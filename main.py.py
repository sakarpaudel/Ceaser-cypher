def welcome():
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text using Caesar Cipher.")

def enter_message():
    valid_modes = {'e', 'd'}
    mode = input("Would you like to encrypt (e) or decrypt (d)? : ").lower()
    
    while mode not in valid_modes:
        print("Invalid Mode")
        mode = input("Would you like to encrypt (e) or decrypt (d)?: ").lower()

    message = input("What message would you like to {} : ".format("encrypt" if mode == 'e' else "decrypt")).upper()

    shift = input("What is the shift number: ")
    while not shift.isdigit() or not (1 <= int(shift) <= 25):
        print("Invalid Shift")
        shift = input("What is the shift number: ")

    return mode, message, int(shift)

def encrypt(message, shift):
    encrypted = ""
    for char in message:
        if char.isalpha():
            shiftvalue = ord(char) + shift
            if char.islower():
                if shiftvalue > ord('z'):
                    shiftvalue -= 26
            elif char.isupper():
                if shiftvalue > ord('Z'):
                    shiftvalue -= 26
            encrypted += chr(shiftvalue)
        else:
            encrypted += char
    return encrypted

def decrypt(message, shift):
    return encrypt(message, -shift)

def write_messages(messages):
    with open("output.txt", "w") as file:
        for message in messages:
            file.write(message + "\n")
    print("Messages written to 'output.txt' successfully.")

def is_file(filename):
    try:
        with open(filename, 'r'):
            pass
        return True
    except FileNotFoundError:
        return False

def process_file(filename, mode):
    messages = []
    with open(filename, 'r') as file:
        for line in file:
            message = line.strip()
            if mode == 'e':
                messages.append(encrypt(message, 1))
            elif mode == 'd':
                messages.append(decrypt(message, 1))
    return messages

def message_or_file():
    valid_modes = {'e', 'd'}
    mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()

    while mode not in valid_modes:
        print("Invalid Mode")
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()

    source = input("Would you like to read from a file (f) or the console (c)? ").lower()

    if source == 'c':
        message = input("What message would you like to {} : ".format("encrypt" if mode == 'e' else "decrypt")).upper()
        return mode, message, None
    elif source == 'f':
        filename = input("Enter a filename: ")
        return mode, None, filename

def main():
    welcome()
    while True:
        mode, message, filename = message_or_file()
        shift = input("What is the shift number: ")
        while not shift.isdigit() or not (1 <= int(shift) <= 25):
            print("Invalid Shift")
            shift = input("What is the shift number: ")

        if filename:
            messages = process_file(filename, mode)
            for result in messages:
                print(result)
        else:
            if mode == 'e':
                encrypted_message = encrypt(message, int(shift))
                print(f"\nEncrypted Message: {encrypted_message}")
            elif mode == 'd':
                decrypted_message = decrypt(message, int(shift))
                print(f"\nDecrypted Message: {decrypted_message}")

        write_messages(messages)

        another_message = input("\nWould you like to {} or decrypt another message? (y/n): ".format("encrypt" if mode == 'e' else "decrypt"))
        if another_message.lower() != 'y':
            print("Thanks for using the program, goodbye!")
            break

main()
