#Coffee menu

menu = "Black Coffee, Espresso, Latte, Cappucino, Frappuccino"
name = "Andrei"

#Ask the customer what they would like from the menu and store it in the variable order.
order = input(name + ", what would you like from our menu today? Here is what we are serving.\n" + menu + "\n")

#Ask the customer how many coffees they would like and store it in the variable QUANTITY
quantity = input("How many coffees would you like?\n")

#Set the price for coffee

if order == "Frappuccino":
    price = 13
elif order == "Black Coffee":
    price = 6
elif order == "Espresso":
    price = 7
elif order == "Latte":
    whipcream = input("Do you want whip creame :")
    if whipcream == "yes":
        price = 13
    else:
        price = 9

elif order == "Cappucino":
    price = 11

else:
    print("Sorry we don't have that here.")
    price = 0

  
print(price)  

