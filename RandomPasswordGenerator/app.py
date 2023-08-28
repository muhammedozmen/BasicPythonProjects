# ask user if they want to generate a password or not
# if the answer is yes, ask for password length
# generate a password
# print the password
# if initial password is no, exit the program

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_length = int(input("How long would you like your password to be? "))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)

option = input("Do you want to generate a password? (y/n): ")

if option == "y":
    generate_password()
elif option == "n":
    print("Program is ended..")
    quit()
else:
    print("Wrong input, please input y or n")
    quit()