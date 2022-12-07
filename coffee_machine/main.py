# data
coffee_names = ['espresso', 'latte', 'cappuccino']

Menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "price": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150,
        },
        "price": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
        },
        "price": 3.0,
    }
}

resources = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
    "money": 0
}


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"coffee: {resources['coffee']}ml")
    print(f"money: ${resources['money']}")

def enough_resources(coffee):
    for ingridient in Menu[coffee]['ingredients']:
        if Menu[coffee]['ingredients'][ingridient] > resources[ingridient]: # if the demand is more than supply, return False.
            return ingridient # return the ingredient that's not enough.
    return True # otherwise, return True.


def avaliable_list():
    output_list = []
    for names in coffee_names:
        counter = 0
        for ingridient in Menu[names]['ingredients']:
            if Menu[names]['ingredients'][ingridient] > resources[ingridient]:
                break # break the nested loop if resources is not enough.
            else:
                counter += 1
        if(counter==len(Menu[names]['ingredients'])):
            output_list.append(names) # append if there is resources to make this certain coffee.

    return output_list



def calculate_coin(quarter,dimes,nickles,pennies,coffee): # coffee is a str type, rest is int type.
    sum = quarter + dimes + nickles + pennies
    coffee_price = Menu[coffee]['price']
    if sum >= coffee_price:
        sum -= coffee_price
        resources['money'] += coffee_price
        return f'Here is ${round(sum,2)} in change.'
    else:
        return "sorry that's not enough money. Money refunded."

def reduce_resources(coffee):
    for ingredient in Menu[coffee]['ingredients']:
        resources[ingredient] -= Menu[coffee]['ingredients'][ingredient]


def coffee_machine():
    operating = True
    while(operating):
        coffee = 'report'
        while(coffee == 'report'):
            coffee = input("What would you like? (espresso/latte/cappuccino): ")
            if(coffee == 'report'):
                report()


        if(len(avaliable_list())==0):
            print("\nOperation done for today! See you tomorrow!")
            break # break out of the while loop since resources are not sufficient.
        elif(coffee not in avaliable_list() or enough_resources(coffee) != True):
            print(f"Sorry there is not enough {enough_resources(coffee)}. {coffee} is not available at the moment.")
            while (coffee not in avaliable_list()):
                print(f'Here is a avaliable list of coffees: {avaliable_list()}. Please choose one of the followings.')
                coffee = input(f'What would you like?: ')
                print("Please insert coins.")
                quarter = int(input("how many quarters?: ")) * 0.25
                dimes = int(input("how many dimes?: ")) * 0.10
                nickles = int(input("how many nickles?: ")) * 0.05
                pennies = int(input("how many pennies?: ")) * 0.01

                print(calculate_coin(quarter, dimes, nickles, pennies, coffee))
                reduce_resources(coffee)
        else:

            print("Please insert coins.")
            quarter = int(input("how many quarters?: ")) * 0.25
            dimes = int(input("how many dimes?: ")) * 0.10
            nickles = int(input("how many nickles?: ")) * 0.05
            pennies = int(input("how many pennies?: ")) * 0.01

            print(calculate_coin(quarter, dimes, nickles, pennies, coffee))
            reduce_resources(coffee)

coffee_machine()
