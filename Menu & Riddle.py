def main():
    MainMenu()

def MainMenu():
    print("Welcome User!\nPlease enter a number from the list:\n")
    menuop = str(input("1 - Riddles\n2 - Trivia:\n"))
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
            print("reuhiurehgf")
        case "3":
            print("shbgifg")
        case _:
            print("Enter a number from the list:\n")
            Riddles()

def EasyRiddle():
    askriddle = str(input(riddles[1]))









if __name__ == "__main__":
    main()
