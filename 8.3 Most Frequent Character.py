def main():
    frequent_letter = ""
    frequency = 0
    count = 0
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    user_string = input(" Please enter a phrase and I will determine the letter used the most: ")

    for letter in alphabet:
        for character in user_string.upper():
            if letter == character:
                count += 1
        if count > frequency:
            frequency = count
            frequent_letter = letter
        elif count == frequency:
            frequent_letter += letter
            count = 0
        else:
            count = 0

    print('The most frequently used letter is: ' + frequent_letter)
    print("It was used " + str(frequency) + " times.")
