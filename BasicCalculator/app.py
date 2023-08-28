# defining the functions needed: add, sub, mul, div
# printing options to the user to choose them
# ask for values
# call the functions
# while loop to continue the program until the user wants to exit

def add(a, b):
    answer = int(a) + int(b)
    print(str(a) + " + " + str(b) + " = " + str(answer))

def sub(a, b):
    answer = int(a) - int(b)
    print(str(a) + " - " + str(b) + " = " + str(answer))

def mul(a, b):
    answer = int(a) * int(b)
    print(str(a) + " * " + str(b) + " = " + str(answer))

def div(a, b):
    answer = int(a) / int(b)
    print(str(a) + " / " + str(b) + " = " + str(answer))

while True:
    print("A, Addition")
    print("B, Subtraction")
    print("C, Multiplication")
    print("D, Division")
    print("E, Exit")

    choice = input("Input your choice: ")

    if choice == "a" or choice == "A":
        print("Addition")
        a = input("Give the first number: ")
        b = input("Give the second number: ")
        add(a, b)
    if choice == "b" or choice == "B":
        print("Subtraction")
        a = input("Give the first number: ")
        b = input("Give the second number: ")
        sub(a, b)
    if choice == "c" or choice == "C":
        print("Multiplication")
        a = input("Give the first number: ")
        b = input("Give the second number: ")
        mul(a, b)
    if choice == "d" or choice == "D":
        print("Division")
        a = input("Give the first number: ")
        b = input("Give the second number: ")
        div(a, b)
    if choice == "e" or choice == "E":
        print("Program is ended..")
        quit()