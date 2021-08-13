"""
The name of this game is Number Guess. 
The computer rolls a pair of dice and asks the user to guess the sum. 
If the user’s guess is equal to the total value of the dice rolls, the user wins! 
Otherwise, the computer wins.
"""

# import code to make sure rolls are random
# import more code to simulate dice rolls
from random import randint
from time import sleep

print('''
Welcome to Number Guess.
Your challenge is to guess the sum of the computer dice rolls.
You win if your guess is equal to the total value of the dice rolls.
Otherwise, the computer wins.
  ''')

# prompt user for guess
def get_user_guess():
  guess = int(input("Please guess a number: "))
  return guess

# build the rest of the game
def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2

  # let user know what the maximum possible value is
  print("The maximum possible value is: %d" % max_val)
  guess = get_user_guess()

  # write the rules that determine the winner
  if guess > max_val:
    print("Sorry. That number is higher than the maximum possible value.")
  else:
    print("Rolling...")
    sleep(2)
    print("The first roll is: %d" % first_roll)
    sleep(1)
    print("The second roll is: %d" % second_roll)
    sleep(1)
    
    # use the total value of dice roll to determine winner
    total_roll = first_roll + second_roll
    print("The total value is: %d" % total_roll)
    print("Result...")
    sleep(1)
    if guess == total_roll:
        print("You won!")
    else:
        print("You lost; try again.")

roll_dice(6)

