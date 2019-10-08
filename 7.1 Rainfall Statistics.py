grand_total = 0

print("This program will calculate total rainfall and average monthly rainfall for a period of years.")


monthly_rainfall = 0
total_rainfall = 0
total_rainfall += monthly_rainfall
average_rainfall = total_rainfall / 12
total = 0

for month in ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"):
    current_rain = int(input('How much rain fell during the month of ' + month + "? "))
    total += current_rain
    average_rainfall = total / 5
    grand_total += current_rain
    print('The total amount of rainfall was:', total)
    print('The average monthly rainfall was:', total / 12)


