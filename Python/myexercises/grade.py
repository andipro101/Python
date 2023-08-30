score = input ("score:")
try:
    fscore = float(score)
except:
    input("Bad Score")
    exit()
if fscore > 1.0:
    print('error')
    exit()
elif fscore >= 0.9:
    print('A')
elif fscore >= 0.8: 
    print('B')
elif fscore >= 0.7: 
    print('C')
elif fscore >= 0.6: 
    print('D')
elif fscore < 0.6: 
    print('F')

#Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:
#  Score   Grade
# >= 0.9     A
# >= 0.8     B
# >= 0.7     C
# >= 0.6     D
#  < 0.6     F

