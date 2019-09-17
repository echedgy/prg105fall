num_months = 0
inches_of_rain = 0
num_years = int(input("how many years would you like to collect data for?"))

print("This program will calculate total rainfall and average monthly rainfall for a period of years.")
for current_year in range(1, num_years + 1):
    for current_month in range(1, 13):
        monthly_rain_inches = float(input("Type the inches of rain in month" + format(current_month, "d") + ", year" + format(current_year, "d") + ": "))
        inches_of_rain += monthly_rain_inches
        num_months += 1

avg_rainfall = inches_of_rain / num_months

print("Your number of months:" + format( num_months, "d"), "Total" + " inches of rain: " + format(inches_of_rain, ".2f"), "average of rain: " + format( avg_rainfall, ".2f"), sep="\n")

