#desk class, subclass of OfficeFurniture
import office_furniture

class Desk(office_furniture.OfficeFurniture):
    def __init__(self, category, material, length, width, price, location, number):
        self.__location_of_drawers = location
        self.__number_of_drawers = number

    office_furniture.OfficeFurniture.__init__(self, category, material, lenth, width, price)

    def set_location_of_drawers(self, location_of_drawers):
        self.__location_of_drawers = location_of_drawers

    def set_number_of_drawers(self, number_of_drawers):
        self.__number_of_drawers = number_of_drawers

    def __str__(self):
        return
