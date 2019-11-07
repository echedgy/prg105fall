#desk class, subclass of OfficeFurniture
#In the second step create a subclass for Desk
# that includes location_of_drawers (left, right both are options) and number_drawers.
# Override the parents __str__ method to include drawer location and count.
import office_furniture

class Desk(office_furniture.OfficeFurniture):
    def __init__(self, category, material, length, width, price, location, number):
        self.__location_of_drawers = location
        self.__number_of_drawers = number

    office_furniture.OfficeFurniture.__init__(self, category, material, length, width, price)

    def set_location_of_drawers(self, location_of_drawers):
        self.__location_of_drawers = location_of_drawers

    def set_number_of_drawers(self, number_of_drawers):
        self.__number_of_drawers = number_of_drawers

    def get_location_of_drawers(self):
        return self.__location_of_drawers

    def get_number_of_draweres(self):
        return self.__number_of_drawers

    def __str__(self):
        return
