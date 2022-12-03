# Blackjack game

## Goal: 

To create a working blackjack game.

## Blackjack rules
* The goal of the game is to add up your number closest or to 21 without going over 21. If the sum goes over 21, you lose.
* Card numbers range between 2-10. Jack, Queen, and King each count as 10. Ace can either count as 1 or 11 and you can choose depending on the situation. 
* To start off, you draw one card and the dealer also draw one card. Both cards are revealed to each other. Second time, you draw another card and dealer draws a card. However, dealer's card is concealed this time. At this point, you know your two cards and also know dealer's first card but not the second card. You can either choose to stop the game here or keep drawing cards until you stop. If the sum of dealer's card after second drawing is less than 17, then the dealer **must** draw another card until sum of the card is more than 17. 

## Implementation

### Model

One array that contains all of the possible numbers. It contains three 10s(Jack,Queen,and King), one 1s and one 11s(Ace), and 2-10(Number cards).


#### Inputs

* Two randomly drawn cards for the user and one randomly drawn card for dealer to start off the game. User can input 'yes' or 'no' to keep drawing cards or not. 


#### Outputs

* After user gave the input 'no', final score and cards are shown for both user and dealer. Game ends and outputs are shown whether user has won the game or not. Then, ask the user if they want to play the blackjack again.
