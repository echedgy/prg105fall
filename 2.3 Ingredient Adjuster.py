# A cookie recipe calls for the following ingredients:
# 1.5 cups of sugar
# 1 cup of butter
# 2.75 cups of flour
# The recipe produces 48 cookies with this amount of ingredients. Write a program that asks the user
# how many cookies they want to make, and then displays the number of cups
# (to two decimal places) of each ingredient needed for the specified number of cookies.
COOKIE_NUMBER = 48

cupsOfSugar_cookie_num = 1.5/COOKIE_NUMBER
cupsOfButter_cookie_num = 1/COOKIE_NUMBER
cupsOfFlour_cookie_num = 2.75/COOKIE_NUMBER
userNumber_of_cookies = int(input('How many cookies do you want to make? '))
print("For " + str(userNumber_of_cookies) + " cookies, you will need")

expectedCupsOfSugar = userNumber_of_cookies * cupsOfSugar_cookie_num
expectedCupsOfButter = userNumber_of_cookies * cupsOfButter_cookie_num
expectedCupsOfFlour = userNumber_of_cookies * cupsOfFlour_cookie_num

print(format(expectedCupsOfSugar, ".2f") + " cups of sugar, " + format(expectedCupsOfButter, ".2f") + " cups of butter and " + format(expectedCupsOfFlour, ".2f") + " cups of flour")
