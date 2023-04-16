# DECRYPTION

# Import string funstion to generate a list.
import string

# Make a list for key.
key = " " + string.punctuation + string.digits + string.ascii_letters
key = list(key)

# Make a duplicate list for keyvalue.
key_values = " " + string.punctuation + string.digits + string.ascii_letters
key_values = list(key_values)

# Change every ! to "u".
key_values [1] = "u"

# Change every # to "i".
key_values [3] = "i"

# Change every & to "e".
key_values [6] = "e"

# Change every * to "a".
key_values [10] = "a"

# Change every + to "o".
key_values [11] = "o"

# Ask user for input message to decrypt.
user_input = input("Please type in a message to decrypt: ")

# Initialize the cipher text.
cipher_text = ""

# Check every character of the input message.
for letter in user_input:
        index = key.index(letter)
        cipher_text += key_values[index]

# Print the decrypted message.
print("The message you inputted: " , user_input)
print("The decrypted message: " , cipher_text)



