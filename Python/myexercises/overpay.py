hours = input("Enter Hours:")
rate = input("Enter Rate:")
fhours = float(hours)
frate = float(rate)
if fhours > 40 :
    ohours = fhours - 40
    whours = fhours - ohours
    overpay = ohours * (frate * 1.5)
    print ('Pay:',whours * frate + overpay)
    exit()
print ('Pay',fhours * frate)

# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0