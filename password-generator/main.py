import random
import string

characters = string.ascii_letters + string.digits + string.punctuation

length = input("Enter password length: ")

if length.isdigit():
    length = int(length)

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("Generated Password:", password)

else:
    print("Please enter numbers only.")
