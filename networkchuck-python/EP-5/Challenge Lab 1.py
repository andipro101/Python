#Bonus Lab Task
#Can you figure out how to correct the mistake in the code?
#Run the code to the see the error!



required_age = 12
print("Welcome to the haunted house!")
age = input("How old are you?" + "\n-->:")


if age >= str(required_age):
  print("Go on in!")
else:
  parent = input("I'm sorry, you are too young. Is your parent here with you?:")
  if parent == 'yes':
    print("Awesome! Go on in!")
  elif parent == 'no':
    print("Sorry, you are too young for the haunted house.")