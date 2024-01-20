# Welcome function to display a message to the user
def welcome():
    print("Welcome to the Caesar Cipher Program!")
    print("This program encrypts and decrypts text using Caesar Cipher.")
    input("Press Enter to Continue!")

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

# Exit point of the program
def end():
    decide = input("Would you like to encrypt or decrypt again? (y/n): ").lower()
    while decide.lower() not in ('y', 'n'):
        print("Please enter 'y' for yes or 'n' for no.")
        decide = input("Would you like to encrypt or decrypt again? (y/n): ").lower()

    if decide == 'y':
        main()
    elif decide == 'n':
        print("Thank you for using this program!!")

# Function to process text input for encryption or decryption
def process_text(mode):
    if mode == "e":
        message = input("Enter the text you want to encrypt: ")
    elif mode == "d":
        message = input("Enter the text you want to decrypt: ")

    shift = input("What is the shift number: ")
    while not shift.isdigit() or not (1 <= int(shift) <= 25):
        print("Error: Shift value must be a number between 1 and 25. Please try again.")
        shift = input("What is the shift number: ")

    if mode == "e":
        print("The Encrypted message is:", encrypt(message, int(shift)))
    elif mode == "d":
        print("The Decrypted message is:", decrypt(message, int(shift)))

    end()

# Function to process file input for encryption
def process_file():
    fname = input('Please enter the name of the file: ')
    try:
        with open(fname, 'r') as f:
            data = f.read()
            encrypted_data = encrypt(data, 1)

        with open("output.txt", "w") as g:
            g.write(encrypted_data)

        print("File successfully encrypted. Encrypted content saved to 'output.txt'.")

    except FileNotFoundError:
        print('Error: File not found! Please check your filename and path.')
    except IOError:
        print('Error: Could not read file. Please ensure the file is not corrupted.')

# Main function
def main():
    welcome()
    user_input = input("Would you like to encrypt (e), decrypt (d), or process a file (f)? : ").lower()

    while user_input not in ('e', 'd', 'f'):
        print("Invalid Mode. Please enter 'e' for encrypt, 'd' for decrypt, or 'f' for file processing.")
        user_input = input("Would you like to encrypt (e), decrypt (d), or process a file (f)? : ").lower()

    if user_input == "e" or user_input == "d":
        process_text(user_input)
    elif user_input == "f":
        process_file()

# Run the main function
main()
