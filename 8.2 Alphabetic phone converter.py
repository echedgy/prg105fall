def main():

    character_list = ['0', '1', '2', 'A', 'B', 'C', '3', 'D', 'E', 'F', '4', 'G', 'H', 'I', '5', 'J', 'K', 'L', '6', 'M', 'N', 'O', '7', 'P', 'Q', 'R', 'S', '8', 'T', 'U', 'V', '9', 'W', 'X', 'Y', 'Z', '-']
    keypad_list = ['0', '1', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '5', '5', '5', '5', '6', '6', '6', '6', '7', '7', '7', '7', '7', '8', '8', '8', '8', '9', '9', '9', '9', '9', '-']
    user_phone = input('Please enter the number so it may be converted (1-800-Get-Food) ')


    phone_out = ''
    for number in user_phone:
        print("number = ", number)
        if number.isalpha():
            number = number.upper()
            print("number upper =", number)
        my_index = character_list.index(number)
        phone_out = phone_out + keypad_list(my_index)

    print("The numeric value of the the number you input is: ", phone_out)


main()
