# This first line is provided for you

hours = float(input("Enter Hours:"))
rate = float(input("Rate Per Hour:"))

if hours <= 40:
    pay = hours*rate
else:
    regular_pay = 40 * rate
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * (rate * 1.5)
    pay = regular_pay + overtime_pay

print(pay)

