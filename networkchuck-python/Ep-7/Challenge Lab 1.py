#You have been tracking the average temperature of your city for a week and the data has been organized in the list below.


temps = [75.2, 76.8, 74.3, 75.6, 76.3, 79.2, 80.3]

#Can you print the temperature for Sunday?
sunday = temps[-1]
print(sunday)


#What about Tuesday, Wednesday, and Friday?
tuesday = temps[1]
wednesday = temps[2]
friday = temps[4]

print(tuesday, wednesday , friday)
print("\n")


#I bet you can't print the last three temperatures using a negative index!

print(temps[-1], temps[-2], temps[-3]) 