def main():
    MainMenu()
    

def MainMenu():
    print("Welcome User!\nPlease enter a number from the list:\n")
    menuop = str(input("1 - Riddles\n2 - Trivia\n"))
    match menuop:
        case "1":
            Riddles()
        case "2":
            print("works")
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
            
        





if __name__ == "__main__":
    main()
