import time

# Stylish welcome message
def welcome():
    print("\n--------------------------------------------------------")
    print("|                Welcome to Caesar Cipher!              |")
    print("| Encrypt and decrypt your messages with a touch of style |")
    print("--------------------------------------------------------\n")
    time.sleep(1)
    input("Press Enter to Begin!")

# Function to encrypt a message
def encrypt(message, shift):
    encrypted = ""
    for char in message.upper():
        if char.isalpha():
            shiftvalue = (ord(char) - 65 + shift) % 26 + 65
            encrypted += chr(shiftvalue)
        else:
            encrypted += char
    return encrypted

# Function to decrypt a message
def decrypt(message, shift):
    return encrypt(message, -shift)

# Exiting the program
def end():
    decide = input("\nWould you like to continue? (e: encrypt, d: decrypt, f: file, x: exit): ").lower()
    while decide.lower() not in ('e', 'd', 'f', 'x'):
        print("Please enter 'e' for encrypt, 'd' for decrypt, 'f' for file, or 'x' to exit.")
        decide = input("Would you like to continue? (e: encrypt, d: decrypt, f: file, x: exit): ").lower()

    if decide == 'e':
        process_text('e')
    elif decide == 'd':
        process_text('d')
    elif decide == 'f':
        process_file()
    elif decide == 'x':
        print("\nThank you for experiencing Caesar Cipher! Have a fantastic day!\n")

# Processing text input for encryption or decryption
def process_text(mode):
    if mode == "e":
        message = input("\nEnter the text you want to encrypt: ")
    elif mode == "d":
        message = input("\nEnter the text you want to decrypt: ")

    shift = input("What is the shift number: ")
    while not shift.isdigit() or not (1 <= int(shift) <= 25):
        print("Error: Shift value must be a number between 1 and 25. Try again.")
        shift = input("What is the shift number: ")

    print("\nProcessing...")
    time.sleep(1)

    if mode == "e":
        print("\nThe Encrypted message is:", encrypt(message, int(shift)))
    elif mode == "d":
        print("\nThe Decrypted message is:", decrypt(message, int(shift)))

    end()

# Processing file input for encryption
def process_file():
    fname = input('\nEnter the name of the file: ')
    try:
        with open(fname, 'r') as f:
            data = f.read()
            encrypted_data = encrypt(data, 1)

        with open("output.txt", "w") as g:
            g.write(encrypted_data)

        print("\nFile successfully encrypted. Encrypted content saved to 'output.txt'.\n")

    except FileNotFoundError:
        print('\nError: File not found! Please check your filename and path.')
    except IOError:
        print('\nError: Could not read file. Please ensure the file is not corrupted.')

# Main function
def main():
    welcome()
    user_input = input("\nWould you like to encrypt (e), decrypt (d), process a file (f), or exit (x)? : ").lower()

    while user_input not in ('e', 'd', 'f', 'x'):
        print("Invalid input. Please enter 'e' for encrypt, 'd' for decrypt, 'f' for file, or 'x' to exit.")
        user_input = input("\nWould you like to encrypt (e), decrypt (d), process a file (f), or exit (x)? : ").lower()

    if user_input == "e" or user_input == "d":
        process_text(user_input)
    elif user_input == "f":
        process_file()
    elif user_input == "x":
        print("\nThank you for experiencing Caesar Cipher! Have a fantastic day!\n")

# Running the main function
main()
