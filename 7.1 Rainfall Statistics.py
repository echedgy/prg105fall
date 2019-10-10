def main():

    monthly_rainfall = []
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    total_rainfall - 0

for month in months:
    rainfall = float(input("Enter rainfall total for the month of " + month + " "))
    monthly_rainfall.append(rainfall)
    total_rainfall += rainfall
# Data processing
    average_rainfall = total_rainfall / 12
    min_rainfall = min(monthly_rainfall)
    max_rainfall = max(monthly_rainfall)
    index_min = monthly_rainfall.index(min_rainfall)
    index_max = monthly_rainfall.index(max_rainfall)
# output
    print("The total rainfall for the year was " + str(total_rainfall))
    print("The avereage rainfall for the year was " + format(average_rainfall, ",.2f"))
    print("The minimum amount of rainfall for the month was " + str(min_rainfall) + " inches."))
    print("The month with the minimum rainfall was " + months[index_min]))
    print("The maximum amount of rainfall for a month was " + str(max_rainfall) + " inch(es)")
    print("The month with the maximum rainfall was " + months[index_max])
