#Let's start a coffe shop tgether!! We're going to build a coffee shop using some new Python programing concepts!!

#Let's build robot Barista!!

#Greet your customer

print("Hello, welcome to NetworkChuck Coffee!!!!")

#Ask your custmoer what tier name is with the input() function and store that in the variable NAME.
name = input("what is your name?\n")

#Greet the customer with their name and thank them for coming in todayh using concatenation.

if name == "Ben":
    print("You're not welcome here Ben!! Get out!!")
    exit()
else:
    print("Hello " + name + " thank you so much for coming in today.\n\n\n")

#Coffee menu
menu = "Black Coffee, Espresso, Latte, Cappucino "

#Ask the customer what they would like from the menu and stone it in the variable order.
order = input(name + ", what would you like from our menu today? Here is what we are serving.\n" + menu + "n")

#Ask thje customer how many coffees they would like and store it in the variable QUANTITY
quantity = input("How many coffees would you like?\n")

#Set the price for coffee
price = 8

#Calculate the cusmoer's total
total = price * int(quantity)

#Give the customer their totaal
print("Thank you. Your toatl is: $" + str(total))

#Final statement
print("Sounds good " + name + ", we'll have your " + quantity + " " + order + " ready for you in a moment.")

