#Bonus Lab Task
#Figure out a way to allow kids under 12 years old to enter the haunted house if they have a parent with them.



required_age = 12
print("Welcome to the haunted house!")
age = int(input("How old are you?" + "\n-->:"))


if age >= required_age:
  print("Go on in!")
else:
    parent = input("Do you have a parent yes or no ? :")
    if parent == "yes":
        print("neat you can go in")
    else:
        print("sorry you are to young")


