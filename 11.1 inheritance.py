# Implement each class in a separate file. # Import these into your main program.
# Your main program should implement and display an instance of each, the parent class and the child class.
import desk
import office_furniture


def main():
    chair = office_furniture.OfficeFurniture('Chair', 'Maple', '24 inches', '24 inches', '32 inches', '$299.00')

    print(chair)

    my_desk = desk.Desk('Desk', 'Oak', '32 Inches', '64 inches', '24 inches', '$599.00', 'left', '3 drawers')

    print(my_desk)


main()
