import random
from art import logo
from replit import clear

#1: Start
print(logo)

# 2: Array of numbers
numbers = [1,11,2,3,4,5,6,7,8,9,10,10,10,10]
user = []
dealer = []
# 3: Start the game
playing = input("Do you want to play a game of Blackjack? Type yes or no: ")
while(playing=="yes"):
  
  # User
  for i in range(2):
    user_num = random.randint(0,len(numbers)-1)
    if(numbers[user_num]==1 or numbers[user_num] == 11):
      user_num = int(input("You got Ace! Do you want it to be 1 or 11? Type 1 or 11: "))
      user.append(user_num)
    else:
      user.append(numbers[user_num])
  # Dealer
  for i in range(2):
    dealer_num = random.randint(0,len(numbers)-1)
    dealer.append(numbers[dealer_num])  

  # show starting output
  print(f"Your cards: {user}, current_score: {sum(user)}")
  print(f"Computer's first card: {dealer[0]}")

  # User: after drawing two cards
  keep_going = input("Type yes to draw another card, type no to end the game: ") # Ask the user before the while loop.
  
  while(keep_going=="yes"):
    user_num = random.randint(0,len(numbers)-1) # Same as above.
    
    if(numbers[user_num]==1 or numbers[user_num] == 11): # Same as above.
      user_num = int(input("You got Ace! Do you want it to be 1 or 11? Type 1 or 11: "))
      user.append(user_num)
    else:
      user.append(numbers[user_num])
      
    keep_going = input("Type yes to draw another card, type no to end the game: ") # Ask the user again.

  # Dealer: after drawing two card
  if(sum(dealer)<17):
    while(sum(dealer)<17):
      dealer_num = random.randint(0,len(numbers)-1)
      dealer.append(numbers[dealer_num])

  # Conclusion
  print(f"\nFinal:\nYour final cards:{user}, final score: {sum(user)}")
  print(f"Dealer's final cards:{dealer}, final score:{sum(dealer)}")
  if(sum(user)>21):
    print("You lost.")
  elif(sum(dealer)>21):
    print("You won! Congrats!")
  elif(sum(user)>sum(dealer)):
    print("You won! Congrats!")
  else:
    print("You lost.")

  # Ask user if they want to play again.
  playing = input("Do you want to play a game of Blackjack? Type yes or no: ")
  
  # If user wants to play again, reset the arrays and clear previous outputs.
  if(playing=="yes"):
    user = []
    dealer = []
    clear()
    print(logo)
