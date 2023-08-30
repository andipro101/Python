#Number Guessing Game: Create a program that generates a random number and allows the user to guess it. Provide feedback on whether the guess is too high or too low.



import random
random_number = random.randint(1,10)

guess = False

while not (guess == True):
    
    guess = int(input ("Guess The Number: "))

    if guess > random_number:
        print ("number is lower")   
        
    if guess < random_number:
        print ("number is higher")

    if guess == random_number:
        print("You guessed it")
        guess = True