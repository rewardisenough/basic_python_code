import hangman_art
import hangman_words
from hangman_art import stages,logo
from hangman_words import word_list
import random



#1:Start.
print(logo)

#2:generate a random word from the word list to guess.
word = word_list[random.randint(0,len(word_list)-1)]
print(word)

# 3: create a list of correct guess.
correct_guess = ["_ " for i in range(len(word))] # list to keep track of correct guesses.
print(correct_guess)

output_str = "" # string that will be outputed to the user.

# 4: game

incorrect = 0 # counter for number of incorrect guesses.
correct = 0 # counter for number of correct guesses.
while(incorrect!=7 and output_str.replace(" ","")!=word): 
  user_guess = input("Guess a letter: ")

  # first edge case: If user input is more than one letter.
  if(len(user_guess)!=1):
    while(len(user_guess)!=1):
      user_guess = input("Your guess is not one letter. Please enter one letter.\nGuess a letter: ")

  # second edge case: If user input is already been guessed correctly.
  for i in range(len(correct_guess)):
    output_str += correct_guess[i]
    output_str +=" "   
  if user_guess in output_str:
    while(user_guess in correct_guess):
      user_guess = input(f"You've already guessed {user_guess} correctly. Please enter a different guess.\nGuess a letter: ")
  
  output_str = "" # resets every round.
  
  for i in range(len(word)): # this loop changes the correct_guess array if user_guess is correct.
    if(user_guess == word[i]):
      correct_guess[i] = user_guess
  
  if(user_guess in word): # if user is correct.
    correct += 1
    print(f"You guessed {user_guess}, that's correct. You keep a life.")
    for i in range(len(correct_guess)):
      output_str += correct_guess[i]
      output_str +=" "
    print(output_str)
    print(stages[incorrect])

    
  if(user_guess not in word): # if user is not correct.
    incorrect += 1
    print(f"You guessed {user_guess}, that's incorrect. You lose a life.")
    for i in range(len(correct_guess)):
      output_str += correct_guess[i]
      output_str +=" "
    print(output_str)
    if(incorrect<7):
      print(stages[incorrect])


# 5: Conclusion
if(incorrect==7):
  print(f"\nYou lost! The correct word was {word}. Try again next time!")
else:
  print(f"\nYou won! You guessed {word} correctly! Congrats!")
