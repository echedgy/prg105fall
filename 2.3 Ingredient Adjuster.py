# A cookie recipe calls for the following ingredients:
# 1.5 cups of sugar
# 1 cup of butter
# 2.75 cups of flour
# The recipe produces 48 cookies with this amount of ingredients. Write a program that asks the user
# how many cookies they want to make, and then displays the number of cups
# (to two decimal places) of each ingredient needed for the specified number of cookies.
sugar = 1.5
butter = 1
flour = 2.75
cookie_num = int(input('How many cookies do you want to make?'))

print("You wil need: " + format(sugar * cookie_num, ', .2f ') + "cups of sugar")
print("you will need:" + format(butter * cookie_num, ', .2f') + "cups of butter")
print("you will need:" + format(flour * cookie_num, ', .2f') + "cups of flour")
