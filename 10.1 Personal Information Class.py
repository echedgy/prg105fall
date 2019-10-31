# Design a class that holds the following personal data: name, address, age, and phone number.
# Write appropriate accessor and mutator methods (get and set).
# Write a program that creates three instances of the class.
# One instance should hold your information and the other
# two should hold your friends or family members' information.
# Just add information, don't get it from the user.
# Print the data from each object, make sure to format the output for clarity and ease of reading.


class Person:
    def __init__(self, name_input, address_input, age_input, phone_input):
        self.__name = name_input
        self.__address = address_input
        self.__age = age_input
        self.__phone = phone_input

    def set_name(self, name_input):
        self.__name = name_input

    def set_address(self, address_input):
        self.__address = address_input

    def set_age(self, age_input):
        self.__age = age_input

    def set_phone(self, phone_input):
        self.__phone(self, phone_input)

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone
    def __str__(self):
        return 'Name: ' + self.__name + "\Address " + self.__address +\
            "\nAge " + self.__age + "\nPhone: " + self.__phone


def main():
    person1 = Person("Eric", "4713 Southhampton Dr. Island Lake", "25", "847-271-9987")
    person2 = Person("Matt", "102 Roxbury Lane, Noblesville", "25", "773-202-LUNA")
    person3 = Person("Pete", "4613 Southhampton Dr. island Lake", "26", "847-921-1551")
    print(person1)
    print()
    print(person2)
    print()
    print(person3)


main()
