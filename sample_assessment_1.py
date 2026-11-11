import time
import random
import datetime

Hearts = 3 ##The number of hearts the player has
Lives = 3 ##The number of lives the player has
sign = "" ##The sign of the operation
operation = "" ##The operation questions are based on
level = 1 ##The level the player is on
questionNum = 1 ##The question the player is on
num1 = 1
num2 = 1
answer = 1
questionsCorrect = 0
questionsWrong = 0
questionsAnswered = 0
gameOvers = 0
message = open("endMessage.txt", "w") 

def randomNumber (min, max): ##Creates a function that generates a random number between the given min and max values
    return random.randint(min, max) 

def delayedPrint (message, delay=0.5): ##Creates a function that prints a message with a delay of 1 second
    print(message)
    time.sleep(delay)

def numberSelect(): 
    global num1
    global num2
    num1 = randomNumber(1, 10)
    num2 = randomNumber(1, 10)
    if operation == "division":
        num2 = randomNumber(1, 10)
        multiples = []
        factor = 1
        for i in range(10):
            multiples.append(num2 * factor)
            factor = factor + 1
        num1 = random.choice(multiples) 


def answerSelect():
    global answer
    while True:  # This ensures the loop continues until a valid input is provided
        try:
            answer = int(input("Please enter your answer: "))  # Convert input to an integer
            break  # Exit the loop if the input is valid
        except ValueError:  # Handle non-integer inputs
            delayedPrint("Please enter a valid number.")


def tutorial (operation): ##creates a function that gives a tutorial question on the operation
    delayedPrint("This is a tutorial question.")
    numberSelect()
    if operation == "addition":
        delayedPrint("Addition is the operation where the values of two numbers are combined")
        sign = "+"
        solution = num1 + num2
        delayedPrint("For example, 2 + 2 = 4")
    elif operation == "subtraction":
        delayedPrint("Subtraction is the operation where the value of one number is removed from the other")
        sign = "-"
        solution = num1 - num2
        delayedPrint("For example, 4 - 2 = 2")
    elif operation == "multiplication": 
        delayedPrint("Multiplication is the operation where the value of one number is multiplied by the other")
        sign = "*"
        solution = num1 * num2
        delayedPrint("For example, 2 * 2 = 4")
    elif operation == "division": 
        delayedPrint("Division is the operation where the value of one number is divided by the other")
        sign = "/"
        solution = num1 / num2
        delayedPrint("For example, 4 / 2 = 2")
    delayedPrint("Now you try!")
    delayedPrint("What is " + str(num1) + " " + sign + " " + str(num2) + "?")
    delayedPrint("(You will not lose a heart for this question)")
    answerSelect()
    if answer == solution:
        delayedPrint("Correct!")
    else:
        delayedPrint("Incorrect, the correct answer is " + str(solution))

def levelOperation (level): ##Creates a function which selects an operation based on the level
    global operation
    if level == 1:
        operation = "addition"
    elif level == 2:
        operation = "subtraction"
    elif level == 3:
        operation = "multiplication"
    elif level == 4:
        operation = "division"

def question(operation): ##Creates a funtion that creates a question on the operation
    numberSelect()
    global questionsAnswered
    questionsAnswered = questionsAnswered + 1
    if operation == "addition":
        solution = num1 + num2
        sign = "+"
    elif operation == "subtraction":
        solution = num1 - num2
        sign = "-"
    elif operation == "multiplication": 
        solution = num1 * num2
        sign = "*"
    elif operation == "division":
        solution = num1 / num2
        sign = "/"
    delayedPrint("What is " + str(num1) + " " + sign + " " + str(num2) + "? ")
    answerSelect()
    if answer == solution:
        delayedPrint("Correct!")
        global questionsCorrect
        questionsCorrect = questionsCorrect + 1
    else:
        delayedPrint("Incorrect, the correct answer is " + str(solution))
        global Hearts
        Hearts = Hearts - 1
        delayedPrint("You have lost a heart.")
        delayedPrint("You have " + str(Hearts) + " hearts left.")
        global questionsWrong
        questionsWrong = questionsWrong + 1



def lostLife(): ##Creates a function that checks if the player has lost a life
    global Hearts
    if Hearts == 0:
        global Lives
        global questionNum
        Lives = Lives - 1
        Hearts = 3
        delayedPrint("You have lost a life.")
        delayedPrint("You have " + str(Lives) + " lives left.")
        questionNum = 1
        

def gameOver():  ##Creates a function that checks if the player has lost all their lives
    global Lives
    if Lives == 0:
        delayedPrint("Game Over")
        delayedPrint("You have lost all your lives.")
        delayedPrint("You will now be sent back to the beginning of the game.")
        global level
        level = 1
        global Hearts
        Hearts = 3
        global questionNum
        questionNum = 1
        global gameOvers
        gameOvers = gameOvers + 1
        Lives = 3



def endMessage(): 
    message = open("endMessage.txt", "w")
    if questionsWrong == 0:
        print("You have answered all the questions correctly!", file=message)
    else:
        print("You have answered " + str(questionsCorrect) + " out of " + str(questionsAnswered) + " questions", file=message)
    if gameOvers > 0:
        print("You have lost " + str(gameOvers) + " lives", file=message)
    print("You started at " + str(startTime) + " and finished at " + str(endTime), file=message)
    print("You took " + str(timeTaken) + " to complete the game", file=message)
    message.close()
    
    message = open("endMessage.txt").read()
    print(message)

startTime = datetime.datetime.now() 

delayedPrint("Welcome to Operations")
name = input("Please enter your name: ")
delayedPrint("Hello " + name + ", let's start the game!")
delayedPrint("The game is simple, you will be given an equation and all you have to do is solve it...")
delayedPrint("There are 5 levels in total, the first four focusing on a single operation each, and the last one being a mix of all four operations.")
delayedPrint("Each level will have 4 questions, as well as an extra tutoral question.")
delayedPrint("You will be given 3 hearts and three lives.")
delayedPrint("Answer a question wrong, lose a heart.")
delayedPrint("Lose all your hearts, lose a life.")
delayedPrint("Lose all your lives, it's game over and you start back at the beginnning.")
delayedPrint("Without further ado, let's get started!")

while level <= 5:
    levelOperation(level)
    delayedPrint("Now starting, level " + str(level) + ", " + operation + ".") 
    tutorial(operation)
    while questionNum < 5:
        delayedPrint("Question " + str(questionNum) + ":")
        question(operation)
        lostLife()
        gameOver()
        questionNum = questionNum + 1
    level = level + 1
    questionNum = 1
    if level == 5:
        delayedPrint("This is a mix of all four operations.")
        delayedPrint("You will be given a random operation for each question.")
        delayedPrint("You will not be given a tutorial question.")
        operations = [1, 2, 3, 4]
        while questionNum <= 4:
            delayedPrint("Question " + str(questionNum) + ":")
            level = random.choice(operations)
            levelOperation(level)
            question(operation)
            lostLife()
            gameOver()
            operations.remove(level)
            questionNum = questionNum + 1
            level = 6   
delayedPrint("Congratulations, you have completed the game!")
endTime = datetime.datetime.now()
timeTaken = endTime - startTime

endMessage()

input("Press enter to exit the game.")
