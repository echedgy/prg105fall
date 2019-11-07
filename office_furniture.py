# In the first step, you will create a parent class. Create a parent class for Office Furniture.
# Set the class variables to be a category
# (desk, chair, filing cabinet would be examples), material, length, width, height, and price.
# Include a method that returns a string about the object.
# Implement the __str__ method (refer to section 10.2 in your book for details).


class OfficeFurniture:
    def __init__(self, category, material, length, width, price):
        self.__category = category
        self.__material = material
        self.__length = length
        self.__width = width
        self.__price = price

    def set_category(self, category):
        self.__category = category

    def set_material(self, material):
        self.__material = material

    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width

    def set_price(self, price):
        self.__price = price

    def get_category(self):
        return self.__category

    def get_material(self):
        return self.__material

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_price(self):
        return self.__price

    def __str__(self):
        return "\nCategory: " + self.__category + "\nMaterial: " + self.__material + "\nLength: " + self.__length + "\nWidth: " + self.__width + "\nPrice: " + self.__price
