import pickle

LOOK_up = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

def main():
    try:
        input_file = open('customer_file.dat', 'rb')
        customers = pickle.load(input_file)
        print(customers)
    except (FileNotFoundError, IOError):
        print("File not found, please add a customer then quit to create the file")
        customers = ()
    choice = 0

    while choice != QUIT:
        choice = menu()

        if choice == LOOK_UP:
            look_up(customers)
        elif choice == ADD:
            add(customers)
        elif choice == CHANGE:
            change(customers)
        elif choice == DELETE:
            delete(customers)
        elif choice == QUIT:
            save(customers)

def menu():
    print()
    print("Customer phone lookup")
    print("----------------------")
    print("1. Look up a customer")
    print("2. Add a new customer")
    print("3. Change a phone number")
    print("4. Delete a customer")
    print("5. Quit the program")

    choice = int(input("Enter the number of your choice:  "))
    while choice < 1 or choice > 5:
        choice = int(input( "enter a valid choice:  "))
    return choice

def look_up(customers):
    name = input ("enter a customer name: ")
    print(customers.get(name, 'Not Found'))


def add(customers):
    name = input("Enter customer name:  ")
    phone = input('Enter customer phone number:  ')
    if name not in customers:
        customers(name) = phone
    else:
        print('That entry currently exists. ')

def change(customers):
    name = input("Enter the customer name:  ")
    if name in customers:
        phone = input('Enter the new phone number: ')
        customers(name) = phone
    else:
        print('The customer is not found. ')

def delete(customers):
    name = input("Enter the customer name: ")
    if name in customers:
        del customers(name)
    else:
        print("That customer was not found. ")

def save(customers):
    print("The data file has been updated with your changes.  ")
    save_file = open('customer_file.dat', 'wb')
    pickle.dump(customers, save_file)
    save_file.close()

main()
