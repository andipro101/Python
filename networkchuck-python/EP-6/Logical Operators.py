

print("Hello, welcome to NetworkChuck Coffe!!!!!!!!!")


name = input("What is your name?\n")



if name == "Ben" or name == "Patricia" or name == "Loki":
    evil_status = input("Are you evil?\n")
    good_deeds = int(input("How many good deeds have you done ?: "))
    if evil_status == "Yes" and good_deeds <4:
        print("You're not welcome here " + name + "!! Get out!!")
        exit()
    else:
        print("Hello " + name + ", thank you so much for coming in today. \n\n\n")

else:
    print("Hello " + name + ", thank you so much for coming in today. \n\n\n")

beard_lenght = int(input("How long is your beard?\n"))

if beard_lenght >= 1:
    print("oh hello good sir, nice beard. You may go to the front of the line.")

