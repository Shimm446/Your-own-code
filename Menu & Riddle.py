def main():
    MainMenu()
    

def MainMenu():
    print("Welcome User!\nPlease enter a number from the list:\n")
    menuop = str(input("1 - Riddles\n2 - Trivia\n"))
    match menuop:
        case "1":
            Riddles()
        case "2":
            Trivia()
        case _:
            print("Enter a 1 or 2\n")
            MainMenu()


def Riddles():
    global riddles
    riddles = ["What five-letter word becomes shorter when you add two letters to it?", "What goes up but never comes down?", "I have keys but no locks. I have space but no room. You can enter, but you can't go inside. What am I?"]
    print("Welcome to Riddles!\n---------------------------------\nChoose the difficulty level\n---------------------------------\n")
    askdiff = str(input("1 - Easy\n2 - Medium\n3 - Hard\n"))
    match askdiff:
        case "1":
            EasyRiddle()
        case "2":
            MediumRiddle()
        case "3":
            HardRiddle()
        case _:
            print("Enter a number from the list:\n")
            Riddles()


def EasyRiddle():
    global againridd
    askriddle = input(riddles[1])
    if (askriddle == "age" or askriddle == "Age" or askriddle == "Your age" or askriddle == "Your Age" or askriddle == "your age"):
        print("Correct!")
        againridd = str(input("Do you want to see another riddle? (y/n)\n"))
        AgainRiddle(againridd)
    else:
        print("Wrong.")
        againridd = str(input("Do you want to see another riddle? (y/n)\n"))
        AgainRiddle(againridd)


def MediumRiddle():
    askmed = input(riddles[0])
    if (askmed == "short" or askmed == "Short" or askmed == "SHORT"):
        print("Correct!")
        againridd = str(input("Do you want to see another riddle? (y/n)\n"))
        AgainRiddle(againridd)
    else:
        print("Wrong.")
        againridd = str(input("Do you want to see another riddle? (y/n)\n"))
        AgainRiddle(againridd)


def HardRiddle():
    askhard = input(riddles[2])
    if (askhard == "A Keyboard" or askhard == "a keyboard" or askhard == "keyboard" or askhard == "Keyboard"):
        print("Correct!")
        againridd = str(input("Do you want to see another riddle? (y/n)\n"))
        AgainRiddle(againridd)
    else:
        print("Wrong.")
        againridd = str(input("Do you want to see another riddle? (y/n)\n"))
        AgainRiddle(againridd)


def AgainRiddle(againridd):
    match againridd:
        case "Y":
            return Riddles()
        case "y":
            return Riddles()
        case "N":
            return MainMenu()
        case "n":
            return MainMenu()
        case _:
            print("Enter y or n.")
            AgainRiddle(againridd)


def Trivia():
    global useranswer
    global trivias
    trivias = ["What was the last name of the first President of the United States?", "What year did the Titanic sink?", "What is the smallest bone in human body?"]
    print("welcome to trivia questions!\n--------------------------------- \nYou have three chances to get the answer right.")
    useranswer = str(input("\nChoose the difficulty level\n-------------\n1-Easy\n2-Medium\n3-Hard\nAnswer:"))
    match useranswer:
        case "1":
            easytriv()
        case "2":
            medtriv()
        case "3":
            hardtriv()
        case _:
            print("try again and enter 1, 2 or 3")
            Trivia()

def easytriv():
    askriddle = input(trivias[0])
    if askriddle == "Washington" or askriddle == "washington":
        print("Correct!")
        againopt()
    else:
        print("Incorrect!")
        againopt()
        

def medtriv():
    askriddle = input(trivias[1])
    if askriddle == "1912":
        print("Correct!")
        againopt()
    else:
        print("Incorrect!")
        againopt()

def hardtriv():
    askriddle = input(trivias[2])
    if askriddle == "Stapes" or askriddle == "stapes":
        print("Correct!")
        againopt()
    else:
        print("Incorrect!")
        againopt()
    


def againopt():
    option= str(input("would you like to try another question? Y for yes and N for main menu: \nY/N: "))
    match option:
        case "Y":
            return Trivia()
        case "y":
            return Trivia()
        case "N":
            return MainMenu()
        case "n":
            return MainMenu()
        case _:
            print("Enter y or n.")
            againopt()
            
        



if __name__ == "__main__":
    main()
