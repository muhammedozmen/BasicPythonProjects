import random

exit = False
user_points = 0
computer_points = 0

while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, scissors or exit: ")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("Game ended.")
        print("You won a total score of " + str(user_points) + " and the computer total score is " + str(computer_points))
        exit = True

    if user_input == "rock":
        if computer_input == "rock":
            print("Your input is rock.")
            print("Computer input is rock.")
            print("It's a tie.")
        elif computer_input == "paper":
            print("Your input is rock.")
            print("Computer input is paper.")
            print("Computer won.")
            computer_points += 1
        elif computer_input == "scissors":
            print("Your input is rock.")
            print("Computer input is scissors.")
            print("You won.")
            user_points += 1
    elif user_input == "paper":
        if computer_input == "rock":
            print("Your input is paper.")
            print("Computer input is rock.")
            print("You won.")
            user_points += 1
        elif computer_input == "paper":
            print("Your input is paper.")
            print("Computer input is paper.")
            print("It's a tie.")
        elif computer_input == "scissors":
            print("Your input is paper.")
            print("Computer input is scissors.")
            print("Computer won.")
            computer_points += 1
    elif user_input == "scissors":
        if computer_input == "rock":
            print("Your input is scissors.")
            print("Computer input is rock.")
            print("Computer won.")
            computer_points += 1
        elif computer_input == "paper":
            print("Your input is scissors.")
            print("Computer input is paper.")
            print("You won.")
            user_points += 1
        elif computer_input == "scissors":
            print("Your input is scissors.")
            print("Computer input is scissors.")
            print("It's a tie.")
    elif user_input != "rock" or user_input != "paper" or user_input != "scissors" or user_input != "exit":
        print("Invalid input!") 