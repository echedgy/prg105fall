# Write an Employee class that keeps data attributes for the following pieces of information:
# Employee name
# Employee number
# Next, Write a class named ProductionWorker that is a subclass of the Employee class.
# The ProductionWorker class should keep data attributes for the following information
# Shift numbered (an integer, such as 1, 2, or 3)
# Hourly pay rate
# The workday is divided into two shifts: day and night.
# The shift attribute will hold an integer value representing the shift that the employee works.
# The day shift is shift 1 and the night shift is shift 2.
# Write the appropriate accessor and mutator methods (get and set) for each class.


class Employee:
    def __init__(self, employee_name, employee_number):
        self.__employee_name = employee_name
        self.__employee_number = employee_number

    def set_employee_name(self, employee_name):
        self.__employee_name = employee_name

    def set_employee_number(self, employee_number):
        self.__employee_number = employee_number

    def get_employee_name(self):
        return self.__employee_name

    def get_employee_number(self):
        return self.__employee_number

    def __str__(self):
        return "\nEmployee Name: " + self.__employee_name + "\nEmployee Number: " + self.__employee_number


class ProductionWorker(Employee):
    def __init__(self, employee_name, employee_number, shift, pay_rate):
        Employee.__init__(self, employee_name, employee_number)

        self.__shift = shift
        self.__pay_rate = pay_rate

    def set_shift(self, shift):
        self.__shift = shift

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate

    def get_shift(self):
        return self.__shift

    def get_pay_rate(self):
        return self.__pay_rate

    def __str__(self):
        return "\nEmployee Name: " + self.get_employee_name() + "\nEmployee Number: " + self.get_employee_number() +\
                "\nShift: " + self.__shift + "\nPay Rate: " + self.__pay_rate
