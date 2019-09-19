grand_total = 0

print("This program will calculate total rainfall and average monthly rainfall for a period of years.")

num_year = int(input("how many years would you like to collect data for?"))
num_month = num_year * 12

for year in range(num_year):
    total = 0
    print('Year ', year + 1)
    for month in ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"):
        current_rain = int(input('How much rain fell during the month of ' + month + "? "))
        total += current_rain
        grand_total += current_rain
    print('The total amount of rainfall was:', total)
    print('The average monthly rainfall was:', total / 12)

print("For " + str(num_year) + " years there was a total of " + format(grand_total, ', .2f') + " inches of rain. There was an average of " + format(grand_total / (num_year * 12)) + " inches of rain per month.")
