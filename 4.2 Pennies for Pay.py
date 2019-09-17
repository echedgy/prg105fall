num_Days_Worked = int( input( "How many days have you worked?" ))
num_of_Pennies = 0

print ( "Day\tSalary\n----\t------" )
for current_Day in range ( num_Days_Worked ):
    pennies_For_Day = 2 ** current_Day
    num_of_Pennies += pennies_For_Day
    print( current_Day + 1, "\t" , pennies_For_Day )
total_pay = num_of_Pennies * 0.01

print ( "\nTotal Pay: $", total_pay, sep= "")

