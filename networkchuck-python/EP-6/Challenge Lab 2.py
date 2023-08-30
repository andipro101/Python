##Lab Challenge##
#If someone is a fan of NetworkChuck, they also have to love Coffee right? Make sure we can get rid of fake fans by making sure they love coffee! But if they claim they like NetworkChuck and don't love coffee, kick them out!


nc_fan = input("Welcome to the NetworkChuck fan club!" + "\n" + "You can only enter if you are a NetworkChuck fan!" + "\n" + "So...... are you a fan of NetworkChuck??:")


if nc_fan == "Yes":
    coffee = input("Do you like coffee ? :")
if nc_fan == "Yes" and coffee == "Yes":
    print("Awesome! Come on in!")
elif nc_fan == "Yes" and coffee != "Yes":
   print("Real NetworkChuck fans love coffee! Get out of here!")

else:
  print("Oh... Too bad.. I guess you came to the wrong fan club.")

