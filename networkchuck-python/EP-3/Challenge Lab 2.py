#task 1 create variable = price and asign a integer /same price
#task 2 program barista to ask how many items on the menu you will like / remember how many
#task 3 program your barista to give you your total
menu = ("black coffee\n" + "white coffee\n" + "ice coffee")
price = 10


name = input("Hello customer what is your name\n" + "name:")
print("\nHello " + name + " here is your menu:\n" + menu)

order = input("\nWhat type of coffee would you want to order?\n" + "order:")
order_count = input("\nHow many coffees would you like\n"+ "order count: ")

print ("\nThank you " + name + " your order of "+ order_count + " " + order + " will be ready in a few moments.")
total = price * int(order_count)
print ("Your total will be: " + str(total) + "$")



