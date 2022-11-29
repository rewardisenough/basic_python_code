#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# ask user for easy or hard
choice = input(f"Type easy if you want a easy level password. Type hard if you want a hard level password.\n")

if(choice!="easy" and choice!="hard"):
  while(choice!="easy" and choice!="hard"):
    print("Type easy or hard.")
    choice = input(f"Type easy if you want a easy level password. Type hard if you want a hard level password.\n")
  

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""
if(choice.lower() == "easy"):
  for i in range(nr_letters):
    password += letters[random.randint(0,len(letters)-1)]
  for i in range(nr_symbols):
    password += symbols[random.randint(0,len(symbols)-1)]
  for i in range(nr_numbers):
    password += numbers[random.randint(0,len(numbers)-1)]
  print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
if(choice.lower()=="hard"):
  arr = [i for i in range(nr_letters+nr_symbols+nr_numbers)]
  for i in range(len(arr)):
    random_num = random.choice(arr)
    if(random_num<nr_letters):
      password += letters[random.randint(0,len(letters)-1)]
      arr.remove(random_num)
    elif(random_num<(nr_letters+nr_symbols) and random_num>=nr_letters):
      password += symbols[random.randint(0,len(symbols)-1)]
      arr.remove(random_num)
    else:
      password += numbers[random.randint(0,len(numbers)-1)]
      arr.remove(random_num)
  print(password)
