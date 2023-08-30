hours = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    fhours = float(hours)
    frate = float(rate)
except:
    print ('Error, please enter numeric input')
    exit()
if fhours > 40 :
    ohours = fhours - 40
    whours = fhours - ohours
    overpay = ohours * (frate * 1.5)
    print ('Pay:',whours * frate + overpay)
    exit()
print ('Pay',fhours * frate)

# Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:
# Enter Hours: 20
# Enter Rate: nine
#Error, please enter numeric input
#Enter Hours: forty
#Error, please enter numeric input