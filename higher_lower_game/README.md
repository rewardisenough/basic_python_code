# higher lower game

## Goal:

To create a higher lower game.

## Rules:
* A and B are randomly drawn at the start and user has to choose either A or B. A and B are names of well known things.
* If the user correctly choose the one that more average monthly searches, then user advances to next round.
* In the next round, previous B becomes A and current B is randomly drawn from the list. 
* This cycle continues until user chooses a incorrect answer.


## Functions:

def evaluate():
Evaluates whether user's choice is correct, then returns True or False.

def game():

Starts the game. Radnomly chooses A and/or B from the list. Keeps a counter of user's score. Ends the game if evaluate is equal to false. 
