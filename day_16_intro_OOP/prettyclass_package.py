from prettytable import PrettyTable # import a class named 'PrettyTable' from the package 'prettytable'.

table = PrettyTable()  # create a object named table from PrettyTable class.
table.add_column("Pokemon name",["Pikachu", "Squirtle", "Charmander"])  # method named 'add_column' from PrettyTable class. 
table.add_column("Type", ["Electric", "Water", "Fire"])  # method named 'add_column' from PrettyTable class.
table.align = 'l' # change the value of an attribute named 'align'.
print(table) # print the object named 'table'.
