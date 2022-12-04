import random 
from replit import clear

def evaluate(attempts,guess_num,actual_num):
  if(guess_num>actual_num):
    print("Too high. Guess again.")
    return attempts - 1
  elif(guess_num<actual_num):
    print("Too low. Guess again.")
    return attempts - 1
  else:
    return 0 # 0 meaning game should be over since user has guessed the number correctly.


def game():
  actual_number = random.randint(1,100)
  attempts = 0
  print("Welcome to the number guessing game!")

  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if(difficulty=="easy"):
    attempts = 10
  else:
    attempts = 5

  while(attempts>0):
    print(f"You have {attempts} attempts remaining to guess the number.")
    user_number = int(input("Make a guess: "))
    attempts = evaluate(attempts,user_number,actual_number)
    
  if(user_number == actual_number):
    print(f"You got it. Answer was {actual_number}.")
  else:
    print("You've ran out of attempts, you lose.")


play_again = 'yes'
while(play_again=='yes'):
  game()
  play_again = input("Do you want to play again? Type 'yes' or 'no': ")
  clear()

  
