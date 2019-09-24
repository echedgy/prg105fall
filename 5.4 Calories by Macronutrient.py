def calculatefatcalories(fatgrams):
    fatcalories = fatgrams * 9
    return fatcalories


def calculatecarbcalories(carbgrams):
    carbcalories = carbgrams * 4
    return carbcalories


def main():
    userfatgrams = float(input("Enter fat grams: "))
    usercarbgrams = float(input("Enter carbohydrate grams: "))

    fatcalories = calculatefatcalories(userfatgrams)
    carbcalories = calculatecarbcalories(usercarbgrams)

    print("\n Calories from Fat: " + format(fatcalories, ".2f") + " calories ", "Calories from Carbs: " + format(carbcalories, ".2f") + " calories ", sep="\n")


main()
