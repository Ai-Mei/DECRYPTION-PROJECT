# DECRYPTION

# Introduction
print ("=" * 150)
print("DECRYPTION")
print ("=" * 150)

print("               ／＞　 フ\33[0m".center(50))
print("               | 　_　_| \33[0m".center(50))
print("          ／` ミ＿xノ \33[0m".center(50))
print("         /　　　　 |\33[0m".center(50))
print("        /　 ヽ　　 ﾉ\33[0m".center(50))
print("        │　　|　|　|\33[0m".center(50))
print("／￣|　　 |　|　|\33[0m".center(50))
print("(￣ヽ＿_ヽ_)__)\33[0m".center(50))
print("＼二\33[0m".center(50))
print(" \n Hi, this is DecrypMate. I am designed to help you decrypt your messages. \n".center(150))
print(" 🐾   " * 20)
print()

# User's decision to start the program.
start = int(input("Are you ready to decrypt your message with me? If so, please press 1 to continue and if you want to know more about me, please feel free to press 2. \n"))
while start  == 2:
    print()
    print("‧₊˚⋅♡𓂃 ࣪ ִֶָ☾."* 10)
    print()
    print("It seems that you want to know more about me. Don't worry, I am more than willing to explain. ".center(150, " "))
    print("First, I will ask you an encrypted message. Then I will try to help you to decrypt your message and show you the decrypted message.".center(150, " "))
    print()
    print("‧₊˚ ⋅♡𓂃 ࣪ ִֶָ☾." * 10)
    print()
    start = int(input("Now, I hope I brought light to you. If you are now ready to decrypt messages with me, hit the 1 button. \n"))
    print()

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
print()
print("Let's go ฅ(•ิo•ิ)ฅ\n")
print()
print()
user_input = input("Please type in a message to decrypt: ")
print()
print()
print()
print("Please wait...")
print("ᶻ 𝗓 𐰁" *5)
print()

# Initialize the cipher text.
cipher_text = ""

# Check every character of the input message.
for letter in user_input:
        index = key.index(letter)
        cipher_text += key_values[index]

# Print the decrypted message.
print("The message you inputted: " , user_input)
print("The decrypted message: " , cipher_text)

print()
print()
print(" /ᐠ - ˕ -マ♡ ꒱ ˎ")
print("Thank you for spending your time with me. Let us meet again if you wish to decrypt more messages in the future! Keep on cracking the mysteries of the world! \nLove, DecrypMate.\n")


