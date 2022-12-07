# Coffee machine project

## Goal:

To create a basic virtual coffee machine.

## Rules:

* Makes 3 hot flavors: Espresso, Latte, and Cappuccino. 
* Price: Espresso($1.50), Latte($2.50), Cappuccino($3.00).
* Resources: Espresso(50ml water, 18g coffee), Latte(200ml water, 24g Coffee, 150ml Milk), Cappuccino(250ml water, 24g Coffee, 100ml Milk).
* Coffee machine starts out with: 300ml water, 200ml Milk, and 100g of Coffee. 
* Coin operated: Only inputs Quarter($0.25), Dime($0.10), Nickel($0.05), Penny($0.01).

## Requirements:
* Print report. Report includes the quantity of resources left(water,milk,and coffee). Also prints out how much money it has earned so far.
* Check if resources are sufficient before making a certain coffee.
* Process coin: Calulate how much user has inputted and calculate the left over. 
* Check if transition is successful: If not enough money, return them the money.
* If transition is successful: Make the coffee and deduct the resources. 1

## Functions:

def report():
prints current quantity of resources left and total earned money so far. 

def enough_resources():
check if resources are sufficient to make the coffee.

def process_coin():
check if user has paid enough money for the coffee. calculate total paid by the user. Then return the apporiate amount of change in combinations of coins.


def coffee_machine():
main space to write codes.
