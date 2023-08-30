score = float(input("Enter Score: "))

if score < 0.0 or score > 1.0:
    print("Error out of range")
elif score >= 0.9:
    grade = "A"
elif score >= 0.8:
    grade = "B"
elif score >= 0.7:
    grade = "C"
elif score >= 0.6:
    grade = "D"
elif score <= 0.6:
    grade = "F"

if grade:
    print("Grade",grade)