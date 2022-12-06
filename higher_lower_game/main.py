from game_data import data
import random
from art import logo, vs
from replit import clear

def evaluate(A,B,user):
  if(user=="A" and data[A]['follower_count']>data[B]['follower_count']):
    return True
  elif(user=="B" and data[A]['follower_count']<data[B]['follower_count']):
    return True
  else:
    return False

def game():
  print(logo)
  counter = 0

  A = random.randint(0,len(data)-1) # index number.
  B = random.randint(0,len(data)-1) # index number.
  while(A==B): # To make sure A and B are not same.
    A = random.randint(0,len(data)-1) # index number.
    B = random.randint(0,len(data)-1) # index number.
  
  while(True):
    print(f"Compare A: {data[A]['name']}, a {data[A]['description']}, from {data[A]['country']}.")
    print(vs)
    print(f"Compare B: {data[B]['name']}, a {data[B]['description']}, from {data[B]['country']}.")
    user_input = input("Who has more followers? Type 'A' or 'B': ")
    
    if(evaluate(A,B,user_input)):
      counter+=1
      A = B # A becomes previous B.
      B = random.randint(0,len(data)-1) # B gets a random number.
      clear()
      print(logo)
      print(f"You're right! Current score: {counter}.")
    else:
      clear()
      break
      
  print(f"Sorry that's wrong. Final score: {counter}")

game()
