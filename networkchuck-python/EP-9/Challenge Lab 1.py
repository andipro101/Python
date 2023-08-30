#Here we have a couple of lists, each list is dedicated to a particular student's test grades for this semester



#Students
yoni_grades = [87,90,86,79,88,22]

lisa_grades = [92,94,89,90,86,23]

george_grades = [73,82,85,74,78,21]

kendra_grades = [63,38,72,65,54,23]

#There was a mistake with the system and it accidentally added a really low test grade for all of the students, can you remove the lowest test grade from all of the student lists?
yoni_grades.remove(22)
lisa_grades.remove(23)
george_grades.remove(21)
kendra_grades.remove(23)


#As a part of a bonus grade, we are allowing each student to drop their lowest score so they can have a better average grade, can you remove the lowest test grade from each list? But make sure the grade is printed out!
print (yoni_grades.pop(3))
print (lisa_grades.pop(-1))
print (george_grades.pop(0))
print (kendra_grades.pop(1))



#Kendra has decided that she is going to drop the class after seeing her average, can you remove all of her test grades and print her list?
print (kendra_grades.clear())

