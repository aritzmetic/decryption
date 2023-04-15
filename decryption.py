# Delera, Aritz B.
# decryptor

# Use while loop for a condition-controlled loop
while True:
    # Ask the name of the user to create a greeting
    name = input("Hi Smart Pipol! what is your name?")
    print("Hi", name, "! AritzMetic is here to help you in decrypting your code!")

    # ask the user to input the encrypted text
    user_encryptedtxt = input("What is the text that you want to decrypt?: ")

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
# use the decrypter() method and save the decrypted text
# print out the decrypted text
# Ask the user if they want to repeat the process
# If the user doesn't want to repeat the process, exit the loop