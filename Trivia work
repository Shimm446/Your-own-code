'''
namne: MahmudulShimanto
start date: 06/05/2024
end date:
description: 
'''
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
        print("correct!")
        againopt()
    else:
        print("incorrect!")
        againopt()
        

def medtriv():
    askriddle = input(trivias[1])
    if askriddle == "1912":
        print("correct!")
        againopt()
    else:
        print("incorrect!")
        againopt()

def hardtriv():
    askriddle = input(trivias[2])
    if askriddle == "Stapes" or askriddle == "Stapes":
        print("correct!")
        againopt()
    else:
        print("incorrect!")
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

def main():
    Trivia()



if __name__ == "__main__":
    main()

