from replit import clear
from art import logo

print(logo)

# 1: start
print("Welcome to the secret auction program.")

# 2: Create a dictionary
history = {}

# 3: get first user input
name = ""
bid = 0
name = input("What is your name?: ")
bid = int(input("What's your bid?: $"))
history[name] = bid

# 4: ask user if there's more, if so, continue getting input
more = input("Are there any other bidders? Type yes or no. ")
while(more=="yes"):
  clear() # clear last input for new user.
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  history[name] = bid
  more = input("Are there any other bidders? Type yes or no. ")

  
# 5: Calulate winner
winner = ""
first = True
for name in history:
  if(first):
    winner = name
    first = False
  if(history[name]>history[winner]):
    winner = name

# 6: Final output
clear()
print(f"The winner is {winner} with a bid of ${history[winner]}.")
