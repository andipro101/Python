##Lab Challenge##
#If someone isn't a fan of NetworkChuck, can you ask if they are a fan of Cameron? If they end up being a fan of Cameron or NetworkChuck let them come in!

nc_fan = input("Welcome to the NetworkChuck fan club!" + "\n" +
               "You can only enter if you are a NetworkChuck fan!" + "\n" +
               "So...... are you a fan of NetworkChuck??:")
if nc_fan != "Yes":
    Cameron_fan = input("Then re you a fan of Cameron")

if nc_fan == "Yes" or Cameron_fan == "Yes":
    print("Awesome! Come on in!")
else:
    print("Oh... Too bad.. I guess you came to the wrong fan club.")
    

