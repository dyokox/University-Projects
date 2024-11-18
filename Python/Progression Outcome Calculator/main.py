import sys
from graphics import *

studentProgress = 0
studentRetriever = 0
studentExclude = 0
studentTrailer = 0
totalStudents = studentExclude + studentProgress + studentRetriever + studentTrailer

passCredit = 0
deferCredit = 0
failCredit = 0

totalCredit = passCredit + deferCredit + failCredit

creditRange = [0, 20, 40, 60, 80, 100, 120]

studentData = [] # List to store each student data


# Displaying a small chunk of information to the user before the program starts 
def intro():
    blank = input("""\tUniversity of Westminster\n\tStudent Version 2023\n\tProgression Outcome Calculator\n\nInformation:\n ! To add a student press y followed by enter\n ! To exit the program press q followed by enter\n ! When leaving the program, the user can select to print student data to a .txt or not\n ! The Histogram will display automatically at the end.\n ! press enter to continue""")

# Displaying the menu of the program to the user
def menu():
    while True:
        userInput = input("""\n\n# --------- ᴹ ᴱ ᴺ ᵁ --------- #\n y\tadd student\n q\texit\n → """).lower()
        if userInput == "y":
            progressValidation()
            fileHandling()
        elif userInput == "q":
            print("Exiting...")
            break
        else:
            print(f"{userInput} is not correct. Please use y or q.")

# Validates the user input
def progressValidation():
    global passCredit, deferCredit, failCredit
    # Checks if the input is integer
    try:
        passCredit = int(input("Pass Credit → "))
        deferCredit = int(input("Defer Credit → "))
        failCredit = int(input("Fail Credit → "))
    except ValueError:
        return "Integer Required. Try again"   
    
    # Checks if the input is valid
    if creditChecker():
        studentData.append([passCredit, deferCredit, failCredit])
        markOutcome = determineOutcome(passCredit, deferCredit, failCredit)
        print(markOutcome)
        studentCount(markOutcome)
        print("\nStudent Added")
        menu()
    else:
        print("Invalid credit values, try again")
        menu()

# Checks if the credit inputed by the user are in the range
def creditChecker():
    if (passCredit not in creditRange or deferCredit not in creditRange or failCredit not in creditRange):
        print("Out of range. Try again")
        return False
    else:
        return True
# Checks if the credit are in the range etc.
def determineOutcome(passCredit, deferCredit, failCredit):
    totalCredit = passCredit + deferCredit + failCredit
    if totalCredit == 120:
        if passCredit == creditRange[6]:
            return "Progress"
        elif passCredit == creditRange[5]:
            return "Progress - Module Trailer"
        if failCredit > creditRange[3]:
            return "Exclude"
        else: 
            return "Do not progress - Module Retriever"
    elif totalCredit != 120:
            return "Incorrect total."

# Adds students in total, to later be displayed in the histogram
def studentCount(markOutcome):
    global studentProgress, studentTrailer, studentRetriever, studentExclude
    if "Progress" in markOutcome:
        studentProgress += 1
    elif "Progress - Module Trailer" in markOutcome:
        studentTrailer += 1
    elif "Do not progress - Module Retriever" in markOutcome:
        studentRetriever += 1
    elif "Exclude" in markOutcome:
        studentExclude += 1
    
    totalStudents = studentExclude + studentProgress + studentRetriever + studentTrailer

# Displays neatly all the progression data
def progressionDisplay():
    print("\n\n# --------- ᴾ ᴬ ᴿ ᵀ ² --------- #\n\n Progression Data")
    for index, data in enumerate(studentData, start = 1):
        print(f"\nStudent:\nPass Credit → {data[0]}\nDefer Credit → {data[1]}\nFail Credit → {data[2]}\n{determineOutcome(data[0], data[1], data[2])}\n")

# Writes the data into a .txt 
def fileHandling():
    print("\n# --------- ᴾ ᴬ ᴿ ᵀ ³ --------- #\n\t File Handling\n\nWriting data")
    file = open("studentProgressionData.txt", 'a')
    print("\nProgression Data")
    for index, data in enumerate(studentData, start = 1):
        file.write(f"\nStudent:\nPass Credit >> {data[0]}\nDefer Credit >> {data[1]}\nFail Credit >> {data[2]}\n{determineOutcome(data[0], data[1], data[2])}\n")
    
    # Will print back what was written in the .txt to the user and display histogram
    userInput = input("\nPrint student \"ProgressionData.txt\" in the terminal? (y or n) → ").lower()
    if userInput == "y":
        with open("studentProgressionData.txt", 'r') as file:
            content = file.read()
            print(content)
            input("\n\n! Press enter to quit")
            histogram()
            exit()
    # Won't print back what's in the .txt to the user, still displays histogram
    elif userInput == "n":
        histogram()
        exit()
    else:
        print(f"{userInput} is not valid. Try again")
        fileHandling()

# Short and cleaner way to call the histogram in the code
def histogram():
    drawHistogram(studentExclude, studentProgress, studentRetriever, studentTrailer)

# Drawing the histogram itself, displaying the data
def drawHistogram(studentExclude, studentProgress, studentRetriever, studentTrailer):
    win = GraphWin("Histogram", 800, 800)
    
    resultsText = Text(Point(150, 50), f"Results: {studentProgress + studentTrailer + studentRetriever + studentExclude} student(s)")
    resultsText.setSize(18)
    resultsText.draw(win)

    progressText = Text(Point(125, 400), "Progress")
    progressText.draw(win)
    trailerText = Text(Point(225, 400), "Trailer")
    trailerText.draw(win)
    retrieverText = Text(Point(325, 400), "Retriever")
    retrieverText.draw(win)
    excludeText = Text(Point(425, 400), "Exclude")
    excludeText.draw(win)

    creditsProgressText = Text(Point(125, 350 - studentProgress * 20 - 10), str(studentProgress))
    creditsProgressText.setSize(15)
    creditsProgressText.draw(win)
    creditsTrailerText = Text(Point(225, 350 - studentTrailer * 20 - 10), str(studentTrailer))
    creditsTrailerText.setSize(15)
    creditsTrailerText.draw(win)
    creditsRetrieverText = Text(Point(325, 350 - studentRetriever * 20 - 10), str(studentRetriever))
    creditsRetrieverText.setSize(15)
    creditsRetrieverText.draw(win)
    creditsExcludeText = Text(Point(425, 350 - studentExclude * 20 - 10), str(studentExclude))
    creditsExcludeText.setSize(15)
    creditsExcludeText.draw(win)

    progressRectangle = Rectangle(Point(100, 350), Point(150, 350 - studentProgress * 20))
    progressRectangle.setFill("#b5dbb2")
    progressRectangle.draw(win)

    trailerRectangle = Rectangle(Point(200, 350), Point(250, 350 - studentTrailer * 20))
    trailerRectangle.setFill("#b2dbc9")
    trailerRectangle.draw(win)

    retrieverRectangle = Rectangle(Point(300, 350), Point(350, 350 - studentRetriever * 20))
    retrieverRectangle.setFill("#bfa588")
    retrieverRectangle.draw(win)

    excludeRectangle = Rectangle(Point(400, 350), Point(450, 350 - studentExclude * 20))
    excludeRectangle.setFill("#bd615e")
    excludeRectangle.draw(win)

    win.getMouse()
    win.close()

# Calling the functions
intro()
menu()
