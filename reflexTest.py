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

def countdownTimer():
    randomTime = random.randint(2,5)
    for i in range(randomTime, 0, -1):
        print(f"{i}")
        time.sleep(1)
    #Yoinked from internet ngl
    os.system('cls' if os.name == 'nt' else 'clear')
    return

def userInputs():
    userName = input("congrats!!! You made top ten. Please enter your name: ")
    userGradYear = input("Please enter your graduation year: ")
    userDate = currentDate()
    return userName, userGradYear, userDate

def checkTop10(timeElapsed):
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
                userName, userGradYear, userDate = userInputs()
                replacedValues.append(userName + ", ")
                replacedValues.append(str(timeElapsed) + ", ")
                replacedValues.append(userGradYear + ", ")
                replacedValues.append(str(userDate) + "\n")
                break
            counter += 1
        except:
            None
            
    del scoreFileLinesTwo[9]
    scoreFileLinesTwo.insert(counter, replacedValues)

    reWriteFile = open("reaction_scores.txt", 'w')
    
    for lines in scoreFileLinesTwo:
        reWriteFile.writelines(lines)
    reWriteFile.close()

    return
    
def gamePart(key):

    countdownTimer()
    print(f"Type in the key {key}")

    startTime = time.time()
    keyboard.wait(key)
    endTime = time.time()
    timeElapsed = endTime - startTime
    print(f"Your time was {(timeElapsed):.4f} ")
    time.sleep(1)
    checkTop10(timeElapsed)

def runGame():
    listofKeys = ["a", "b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    checkReady()

    newKey = randomKey(listofKeys)

    gamePart(newKey)
    os.system("start reaction_scores.txt")
    playAgain = input("Would you like to play again? y/n: ")
    if playAgain.lower() == "yes" or playAgain[0].lower() == "y":
        runGame()
    else:
        print("Thanks for playing!")
        return
        
printInstructions()
runGame()