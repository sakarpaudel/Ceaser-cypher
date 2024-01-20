def welcome():
    """welcome function to print display message to the user"""
    print("Welcome to the Caesar Cipher \nThis program encrypts and decrypts text using Caesar Cipher. ")
    input("Press Enter to Continue!")

def encrypt(message,shift):
    '''this function encrypts a message '''
    encrypted = ""
    for char in message.upper():
        if char.isalpha():
            shiftvalue = ord(char) + shift
            if shiftvalue > 90 :
                afterz = shiftvalue - 26
                encrypted += chr(afterz)
            elif shiftvalue < 65:
                aftera = shiftvalue + 26
                encrypted += chr(aftera)
            else:
                encrypted += chr(shiftvalue)
        else:
            encrypted += char
    return(encrypted)

def decrypt(message,shift):
        '''this function decrypts a message'''
        return encrypt(message,-shift)

def end():
    '''This is the exit point of the program'''
    decide=input("would you like to encrypt or decrypt again? (y/n): ").lower()#if the user wants to continue?
    while type(decide) != str:
        print("enter a valid input!!!")
        decide=input("would you like to encrypt or decrypt again? (y/n): ").lower()
        
    while decide.lower() not in ('y','n'): #if user wants to continue it run
        print("enter a valid input!!!")
        decide=input("would you like to encrypt or decrypt again? (y/n): ").lower()
    
    if decide == 'y':
        main()
        # decide=input("Would you like to continue with Encrypt(e) or Decrypt(d) ?(y/n)").lower()
    elif decide == 'n':     
        print("thank you for using this program!!")#runs if the user want to stop the program
        
def file():
    '''This function opens a .txt file, reads its content, and asks the user to either encrypt or decrypt.'''
    fname = input('Please enter the name of the file: ')
    
    try:
        with open(fname, 'r') as f:
            data = f.read()
            print("File Content:\n", data)
            
        action = input("Do you want to encrypt (e) or decrypt (d) the file content? : ").lower()
        while action not in ('e', 'd'):
            print("Invalid action.")
            action = input("Do you want to encrypt (e) or decrypt (d) the file content? : ").lower()
        
        while True:
            shift = input("What is the shift number: ")
            if shift.isdigit() and 1 <= int(shift) <= 25:
                if action == 'e':
                    encrypted_data = encrypt(data, int(shift))
                    print("The Encrypted content is:", encrypted_data)
                elif action == 'd':
                    decrypted_data = decrypt(data, int(shift))
                    print("The Decrypted content is:", decrypted_data)
                break
            else:
                print("Error: Shift value must be a number between 1 and 25. Try again.")
        
    except FileNotFoundError:
        print('File does not exist! Please check your filename and path.')
    except IOError:
        print('Could not read file. Please ensure the file is not corrupted.')

def process_text(mode):
    '''Processes text input for encryption or decryption.'''
    if mode == "e":
        message = input("Enter the text you want to encrypt: ")
    elif mode == "d":
        message = input("Enter the text you want to decrypt: ")

    while True:
        shift = input("What is the shift number: ")
        if shift.isdigit() and 1 <= int(shift) <= 25:
            if mode == "e":
                print("The Encrypted message is", encrypt(message, int(shift)))
            elif mode == "d":
                print("The Decrypted message is", decrypt(message, int(shift)))
            break
        else:
            print("Error: Shift value must be a number between 1 and 25. Try again.")

    end()

def process_file():
    '''Processes file input for encryption.'''
    fname = input('Please enter the name of the file: ')
    try:
        with open(fname, 'r') as f:
            data = f.read()
            encrypted_data = encrypt(data, 1)
        
        with open("output.txt", "w") as g:
            g.write(encrypted_data)
        
        print("File successfully encrypted. Encrypted content saved to 'output.txt'.")
        
    except FileNotFoundError:
        print('File does not exist! Please check your filename and path.')
        input("Press Enter to try again!")
        process_file()
    except IOError:
        print('Could not read file. Please ensure the file is not corrupted.')
        input("Press Enter to try again!")
        process_file()
def main():
    '''This function is the main part of the program'''
    welcome()
    user_input = input("Would you like to encrypt (e), decrypt (d), or process a file (f)? : ").lower()

    while user_input not in ('e', 'd', 'f'):
        print("Invalid Mode")
        user_input = input("Would you like to encrypt (e), decrypt (d), or process a file (f)? : ").lower()

    if user_input == "e" or user_input == "d":
        process_text(user_input)
    elif user_input == "f":
        process_file()

main()

