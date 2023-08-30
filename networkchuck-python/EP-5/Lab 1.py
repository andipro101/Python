#Ask your customer what their name is with the input() function and store that in the variable NAME.
name = input("What is your name?\n")

#Greet the customer with their name and thank them for coming in today using concatenation.

if name == "Ben":
    Evil = input("Are you evil, yes or no :")
    if Evil == "yes":
        print("\nYou're not welcome here Ben!! Get out!!")
        exit()
    else:
        print("\nWelcome our lord " + name + " we are ever so grateful of your presence")
else:
    print("\nHello " + name + ", thank you so much for coming in today.\n")




    
