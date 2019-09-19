total_earned = 0.01
SALARY = 0.01
daily_income = 0  # accumulator

num_days = int(input("How many days have you worked?"))
# day += 1
print("Days Worked | Amount Earned That Day")
for day in range(1, (num_days + 1)):

    if day == 1:
        daily_income = SALARY

    else:
        daily_income *= 2
        total_earned += daily_income
    print(format(day, "5,d") + " | $" + format(daily_income, "30,.2f"))

print("Total earned over " + str(num_days) + " days is $", format(total_earned, " ,.2f"))
