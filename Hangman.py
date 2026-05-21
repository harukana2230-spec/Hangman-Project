import random

countries = ["Austria", "Belgium", "Bulgaria", "Cyprus", "Czech Republic", "Denmark", "Germany", "Estonia", "Greece", "Spain", "Finland", "France", "Hungary", "Ireland", "Italy", "Croatia", "Lithuania", "Luxemburg", "Latvia", "Malta", "The Netherlands", "Poland", "Portugal", "Romania", "Sweden", "Slovenia", "Slovakia"]

#added stages to illustrate hangman
stages = [
"""
  -----
  |   |
      |
      |
      |
      |
---------
""",
"""
  -----
  |   |
  O   |
      |
      |
      |
---------
""",
"""
  -----
  |   |
  O   |
  |   |
      |
      |
---------
""",
"""
  -----
  |   |
  O   |
 /|   |
      |
      |
---------
""",
"""
  -----
  |   |
  O   |
 /|\  |
      |
      |
---------
""",
"""
  -----
  |   |
  O   |
 /|\  |
 /    |
      |
---------
""",
"""
  -----
  |   |
  O   |
 /|\  |
 / \  |
      |
---------
"""
]

score = 0

#randomly choose a word from the list of countries
def choose_word():
  return random.choice(countries).lower()

#added a rules function to explain the game to the user
def show_rules():
  print("\nRules")
  print("Guess the country letter by letter")
  print("Each wrong guess reduces your tries. You have 6 tries in total.")
  print("Try to guess the word before you run out of tries!")

#added a function to get valid input from the user
#isalpha() checks if the input is a letter, and len() checks if it's a single character
def get_valid_input(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower().strip()
        if guess == "":
            print("Please enter a letter.")
        elif len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        elif guess in guessed_letters:
            print("You already tried that letter. Please enter a different letter.")
        else:
            return guess


def play_game():
  #global keyword makes the variable accessible outside the function
  global score

  answer = choose_word()
  guessed_letters = []

#for illustration, reduced tries from 8 to 6
  tries = 6

  print("Welcome to Hangman Game!")
  print("Current score: ", score)

  while tries > 0:
      print(stages[6 - tries])
      print("Tries left:", tries)
      
      display_word = ""

      for letter in answer:
          if letter == " ":
              display_word += " "
          elif letter in guessed_letters:
              display_word += letter
          else:
              display_word += "_"

      print("\nWord:", display_word)
      #To show which letter has been checked already
      print("Guessed letters:", " ".join(guessed_letters))
      print("Score:", score)

      if "_" not in display_word:
          print("You won! The word was:", answer.title())
          score += 1
          print("Your score is now:", score)
          return

      guess = get_valid_input(guessed_letters)
      guessed_letters.append(guess)

      
      if guess not in answer:
          tries -= 1
          print("That letter is not in the word. Tries left:", tries)

  #for the final illustration
  print(stages[6])
  print("You lost! The word was:", answer.title())

def menu():
    while True:
        print("\nMenu")
        print("1. Play Game")
        print("2. Show Rules")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ").strip()

        if choice == "1":
            play_game()
        elif choice == "2":
            show_rules()
        elif choice == "3":
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            
#Call menu function to start the game
menu()


