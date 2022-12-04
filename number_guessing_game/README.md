# Number guessing game

## Goal:

To create a number guessing game.

## Rules:
* Guess an unknown number between 1 and 100.
* Easy mode gets 10 chances to guess and hard mode gets 5 chances.
* User makes a guess and program outputs if the guess is higher or lower than the actual number.
* If user run out of avaliable attempts without guessing the correct number, game ends.


## Functions:

#### Start():
Greets user and generate a random number between 1 and 100 then store it into a variable.

#### user_input():
Ask the user to guess a number. Keeps a counter of how many attempts are left or whether game should be ended. Calculate if user's guess is lower, higher, or equal to the goal number.

#### Conclusion():
If the user guessed the correct number, then print f"You got it! The answer was {answer}." Then, ask the user if they want to play again.
If not, print "You've run out of guesses, you lose. Then, ask the user if they want to play again.
