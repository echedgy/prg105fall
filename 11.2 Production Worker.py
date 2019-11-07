# Once you have written the classes, write a program that creates an object of the ProductionWorker class and prompts
# the user to enter data for each of the object’s data attributes.
# Store the data in the object and then use the object’s accessor methods to retrieve it and display it on the screen.
import employee


def main():

    name = input("Employee's name: ")
    number = input("Employees's number: ")
    shift = input("Employees's Shift: ")
    pay = input("Employee's pay rate: ")

    new_employee = employee.ProductionWorker(name, number, shift, pay)
    print("\nEmployee name: " + new_employee.get_employee_name() + "\nEmployee Number: " + new_employee.get_employee_number() + "\nShift: " + new_employee.get_shift() + "\nPay Rate: " + new_employee.get_pay_rate())


main()
