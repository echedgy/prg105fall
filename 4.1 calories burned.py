# calories burned a minute = 4.2
# write a program that uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.
calories_Burned_per_Minute = 4.2

for number_Of_Minutes in range(10, 31, 5):
    number_Of_Calories_Burned = number_Of_Minutes * calories_Burned_per_Minute
    print( "The calories burned in", number_Of_Minutes, "minutes is", number_Of_Calories_Burned, "calories")
