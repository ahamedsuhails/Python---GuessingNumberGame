import random
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5

def check_guess(actualguess, guess, difficulty):
  if guess > actualguess:
    print("High")
    return difficulty - 1
  elif guess < actualguess:
    print("Low")
    return difficulty - 1
  else:
    print(f"You guessed right. The answer was {guess}")


def check_level():
  level = input("Enter the difficulty level (easy/hard): ")
  if level == 'easy':
    return EASY_LEVEL
  else:
    return HARD_LEVEL


def game():
  print(logo)
  print("Welcome to the number guessing game")
  computer_guess = random.randint(1,100)
  turns = check_level()
  user_guess = 0
  while computer_guess != user_guess:
    print(f"You have {turns} attempts remaining to guess the number !!")
    user_guess = int(input("Enter your guess: "))
    turns = check_guess(computer_guess, user_guess, turns) 
    if turns == 0:
      print("You have run out of the guesses, You lose")
      return
    elif user_guess != computer_guess:
      print("Guess again")


game()