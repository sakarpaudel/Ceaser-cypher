def welcome():
    """welcome function to print display message to the user"""
    print("Welcome to the Caesar Cipher \nThis program encrypts and decrypts text using Caesar Cipher. ")

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
    return(encrypt)
    print(encrypted)

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

def main():
    '''this function is the main part of the program'''
    user_input = input("Would you like to encrypt (e) or decrypt (d)? : ").lower()

    while user_input.lower() not in ('e','d'):
        print("Invalid Mode")
        user_input = input("Would you like to encrypt (e) or decrypt (d)? : ").lower()

    if user_input == "e":
            message = input("Enter the text you want to encrypt:")
            while True:
                shift = input("What is the shift number: ")
                if shift.isdigit() and 1 <= int(shift) <= 25:
                    encrypt(message,int(shift))
                    break
                else:
                    print("Error: Shift value must be a number between 1 and 25. Try again.")
            

    elif user_input == "d":
            message = input("Enter the text you want to decrypt:")
            while True:
                shift = input("What is the shift number: ")
                if shift.isdigit() and 1 <= int(shift) <= 25:
                    decrypt(message,int(shift))
                    break
                else:
                    print("Error: Shift value must be a number between 1 and 25. Try again.")


    
    end()

def file():
    '''This function opens a .txt file and reads its content then calls the main function'''
    fname = input('Please enter the name of the file: ')
    try:
        with open(fname,'r') as f:
            data = f.read()#.replace('\n', '') #removes new lines from the
                #file so that it can all fit on one line
            h = encrypt(data,1)
        with open("output.txt","a")as g:
            g.write(str(h))
    except FileNotFoundError:
        print('File does not exist! Please check your filename and path.')
    except IOError:
        print('Could not read file. Please ensure the file is not corrupted.')
    file()

file()
