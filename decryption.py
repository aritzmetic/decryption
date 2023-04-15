# Delera, Aritz B.
# decryptor

# import pyfiglet module
import pyfiglet

opening = pyfiglet.figlet_format("= O.O.P =", font = "lean")
print(opening)


# Create an introduction
print("=" * 51)
print("\033[32m Welcome to AritzMetic's Decrypter! \033[0m".center(60, "+"))
print("=" * 51)

# Use while loop for a condition-controlled loop
while True:
    # Ask the name of the user to create a greeting
    name = input("\033[34mHi Smart Pipol! what is your name?\033[0m")
    print("\033[40mHi", name, "! AritzMetic is here to help you in decrypting your code!\033[0m")

    # ask the user to input the encrypted text
    user_encryptedtxt = input("\033[31mWhat is the text that you want to decrypt?: \033[0m")

    # Make a decryption class that we will be using for the program
    class Decryption:
        def __init__(self, user_encryptedtxt):
            # we need to initialize the instance variable
            self.encrypted_text = user_encryptedtxt

        # create a method to decrypt the encrypted text
        def decrypter(self):
            user_decryptedtxt = ""
            for character in user_encryptedtxt:
            # check if the character matches any of the substitution characters, Change '*' to 'a'
                if character == '*':
                    user_decryptedtxt += 'a'
                # Change '&' to 'e'
                elif character == '&':
                    user_decryptedtxt += 'e'
                # Change '#' to 'i'
                elif character == '#':
                    user_decryptedtxt += 'i'
                # Change '+' to 'o'
                elif character == '+':
                    user_decryptedtxt += 'o'
                # Change '!' to 'u'
                elif character == '!':
                    user_decryptedtxt += 'u'
                # Put the character in place if it isn't a replacement character
                else:
                    user_decryptedtxt += character
            # return the decrypted text
            return user_decryptedtxt

    # make a new instance of the Decrypter class using the encrypted text
    decrypt = Decryption(user_encryptedtxt)
    # use the decrypter() method and save the decrypted text
    inputted_text = decrypt.decrypter()
    # print out the decrypted text
    print("\033[40mYown! The process has been completed!", inputted_text,"is your plain text!\033[0m")
    # Ask the user if they want to repeat the process
    question = input("\033[36mWould you like to repeat the process? (yes or no): \033[0m")
    # If the user doesn't want to repeat the process, exit the loop
    if question.lower() == "no":
        closing = pyfiglet.figlet_format("Thank you for using AritzMetic's Decrypter. Have a nice day!", font="puffy")
        print(closing)
        quit()