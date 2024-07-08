import keyboard
import random 
import time 
from datetime import datetime
import os

def checkReady():
    while True:
        userAnswer = input("Are you ready? y/n: ")
        if userAnswer.lower() == "yes" or userAnswer[0].lower():
            return
        else:
            print("Well then wait until your ready...")
            
def printInstructions():
    print("This is a reaction test, please wait for the countdown and then try to press the random key as fast as possible. You dont have to press enter. Good Luck!")

def randomKey(list):
    randomKey = random.choice(list)
    return randomKey

def currentDate():
    dateNow = datetime.date(datetime.now())
    return dateNow

def countdownTimer(key):
    randomTime = random.randint(2,5)
    for i in range(randomTime, 0, -1):
        print(f"{i}")
        time.sleep(1)
    #Yoinked from internet ngl
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Type in the key {key}")
    return

def userInputs():
    userName = input("Please enter your name: ")
    while True:
        try:
            userGradYear = int(input("Please enter your graduation year: "))
            break
        except:
            print("Please enter a integer.")
    userDate = currentDate()
    return userName, userGradYear, userDate

def checkTop10(timeElapsed, userName, userGradYear, userDate):
    replacedValues = []
    scoreFile = open("reaction_scores.txt", "r")
    scoreFileLines = scoreFile.readlines()
    scoreFile.close()

    scoreFile = open("reaction_scores.txt", "r")    
    scoreFileLinesTwo = scoreFile.readlines()
    scoreFile.close()

    for i in range(len(scoreFileLines)):
        scoreFileLines[i] = scoreFileLines[i].split(",")

    counter = 0
    for listInfo in scoreFileLines:
        try:
            if timeElapsed < float(listInfo[1]):
                print("You have made it into the top10!")
                replacedValues.append(userName + ", ")
                replacedValues.append(str(timeElapsed) + ", ")
                replacedValues.append(userGradYear + ", ")
                replacedValues.append(str(userDate) + "\n")

                del scoreFileLinesTwo[-1]
                scoreFileLinesTwo.insert(counter, replacedValues)

                reWriteFile = open("reaction_scores.txt", 'w')
    
                for lines in scoreFileLinesTwo:
                    reWriteFile.writelines(lines)
                    
                reWriteFile.close()

                break
            counter += 1
        except:
            None
        else:
            None
    myFile = open("reaction_scores.txt", 'r')
    textFile = myFile.read()
    print(textFile)
    return
    
def gamePart(key, userName, userGradYear, userDate):

    countdownTimer(key)
    startTime = time.time()
    keyboard.wait(key)
    endTime = time.time()

    timeElapsed = endTime - startTime
    print(f"Your time was {(timeElapsed):.4f} seconds. ")
    time.sleep(.3)

    checkTop10(timeElapsed, userName, userGradYear, userDate)

def runGame(userName, userGradYear, userDate):
    listofKeys = ["a", "b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    checkReady()
    newKey = randomKey(listofKeys)

    gamePart(newKey, userName, userGradYear, userDate)
    playAgain = input("Would you like to play again? y/n: ")
    if playAgain.lower() == "yes" or playAgain[0].lower() == "y":
        runGame(userName, userGradYear, userDate)
    else:
        print("Thanks for playing!")
        return

printInstructions()
userName, userGradYear, userDate = userInputs()
runGame(userName, userGradYear, userDate)