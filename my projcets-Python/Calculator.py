#Calculator: Build a simple calculator program that can perform basic arithmetic operations like addition, subtraction, multiplication, and division based on user input.

start = "Yes"


first_number = float(input("first number: "))
operation = input("operation: ")
second_number = float(input("second number: "))

if operation == "+":
    score = (first_number + second_number)
    print("= " + str(score))
elif operation == "-":
    score = (first_number - second_number)
    print("= " + str(score))
elif operation == "*":
    score = (first_number * second_number)
    print("= " + str(score))
elif operation == "/":
    score = (first_number / second_number)
    print("= " + str(score))
else:
    print("error")

cont = input("If you want to continue type Yes: ")

while cont == "Yes":
    print (score)
    operation = input("operation: ")
    second_number = float(input("second number: "))
    if operation == "+":
        new_score = (score + second_number)
        score = new_score
        print("= " + str(score))
    elif operation == "-":
        new_score = (score - second_number)
        score = new_score
        print("= " + str(score))
    elif operation == "*":
        new_score = (score * second_number)
        score = new_score
        print("= " + str(score))
    elif operation == "/":
        new_score = (score / second_number)
        score = new_score
        print("= " + str(score))
    else:
        print("Error")
    
    cont = input("\nDo you want to continue: ")
        

    










 