package = input("Which package do you have? (A, B, C): ")
print("You entered Package " + package)
minutes_used = int(input("How many minutes did you use this month? "))
package_price = 0.0

if package == "A" or package == "a":
    package_price = 39.99
    if minutes_used > 450:
        additional_minutes = minutes_used - 450
        minutes_cost = additional_minutes * .45
        total_cost = package_price + minutes_cost
        print("With package " + package + " and " + str(minutes_used) + " minutes used, you owe: $" + format(total_cost, ',.2f'))
    else:
        print("With package " + package + " and " + str(minutes_used) + " minutes used, you owe: $" + format(package_price, '.2f'))
elif package == "B" or package == "b":
    package_price = 59.99
    additional_minutes = minutes_used - 900
    minutes_cost = additional_minutes + .40
    total_cost = package_price + minutes_cost
    print("With package " + package + " and " + str(minutes_used) + " minutes used, you owe: $" + format(total_cost, '2.f'))

elif package == "C" or package == "c":
    package_price = 69.99
    print("With package " + package + " you owe: $" + format(package_price, ' .2f'))
else:
    print("That is not a valid package.")
