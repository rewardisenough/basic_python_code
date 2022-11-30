import hangman_art
from hangman_art import stages,logo
from hangman_words import word_list
import random



#1:Start.
print(logo)

#2:generate a random word from the word list to guess.
word = word_list[random.randint(0,len(word_list)-1)]
print(word)

correct_guess = ["_ " for i in range(len(word))] # list to keep track of correct guesses.
print(correct_guess)

output_str = ""   





user_guess = input("Guess a letter: ") # current guessed letter
for i in range(len(word)):
    if(user_guess == word[i]):
      correct_guess[i] = user_guess


for i in range(len(correct_guess)):
  output_str += correct_guess[i]
  output_str +=" "
print(output_str)

#3:game 
'''
incorrect = 0 
while(incorrect!=7): # 7 lives are given every game.
  cur_guess = input("Guess a letter: ") # current guessed letter
  
  if(len(cur_guess)>1):
    while(len(cur_guess==1)):
      print("Please input only one letter.")
  if(len(cur_guess))
  if(cur_guess.lower() in word):
    print(f"You guessed {cur_guess}. That's correct.")
    print(stages[incorrect]) # stages[0] means 0 incorrect...
  
  
  for i in range(len(word)):
    if(correct_guess == word[i]):
      correct_guess[i*2] = cur_guess
  
  if(cur_guess.lower() not in word):
    print(f"You guessed {cur_guess}. That's incorrect. You lose a life.")
    incorrect += 1 # incremment incorrect
    print(stages[incorrect]) # stages[0] means 0 incorrect...
  
'''
