# a dictionary that stores questions and answers
# have a variable that tracks the score of the user
# loop through the dictionary using the key values pairs
# display each question to the user and allow them to answer
# tell them if they are right or wrong
# show the final result when the quiz is completed


quiz = {
    "question1": {
        "question": "What is the capital of Turkey?",
        "answer": "Ankara"
    },
    "question2": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question3": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "question4": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question5": {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },
    "question6": {
        "question": "What is the capital of England?",
        "answer": "London"
    },
    "question7": {
        "question": "What is the capital of Portugal?",
        "answer": "Lisbon"
    },
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print('Correct')
        score = score + 1
        print("Your score : " + str(score))
        print("")
        print("")
    else:
        print("Wrong!")
        print("The answer is : " + value['answer'])
        print("Your score : " + str(score))
        print("")
        print("")

print("You got " + str(score) + " out of 7 questions correctly.")
print("Your percentage is " + str(int(score / 7 * 100)) + "%")