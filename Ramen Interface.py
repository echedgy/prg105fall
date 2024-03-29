# Create an original program that uses most of the skills that you have used in this class. The project must:
#
# Use a GUI interface
# Be object oriented
# Use an external file
# Use Functions
# Be well documented (appropriate names and comments)
# Use looping structures
# Use data structures
# Clean code, no warnings


import tkinter


class Ramen:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.drink_frame = tkinter.Frame(self.main_window, bg="yellow")
        self.app_frame = tkinter.Frame(self.main_window, bg="yellow")
        self.ramen_frame = tkinter.Frame(self.main_window, bg="yellow")
        self.size_frame = tkinter.Frame(self.main_window, bg="yellow")
        self.add_ons_frame = tkinter.Frame(self.main_window, bg="yellow")
        self.order_frame = tkinter.Frame(self.main_window, bg="yellow")
        self.charges_frame = tkinter.Frame(self.main_window, bg="yellow")
        self.main_window.title("Take Out Menu")
        self.main_window.configure(background="yellow")
        # apps amd checkbox variables
        self.gyoza_var = tkinter.IntVar()
        self.house_salad_var = tkinter.IntVar()
        self.egg_rolls_var = tkinter.IntVar()
        self.edamame_var = tkinter.IntVar()
        self.yakitori_var = tkinter.IntVar()

        self.gyoza_var.set(0)
        self.house_salad_var.set(0)
        self.egg_rolls_var.set(0)
        self.edamame_var.set(0)
        self.yakitori_var.set(0)

        self.app_label = tkinter.Label(self.app_frame, text="Appetizers", bg="yellow", fg="blue", font="Calibri 16 bold")
        self.gyoza = tkinter.Checkbutton(self.app_frame, text='Gyoza', bg="yellow", variable=self.gyoza_var)
        self.house_salad = tkinter.Checkbutton(self.app_frame, text='House Salad', bg="yellow", variable=self.house_salad_var)
        self.egg_rolls = tkinter.Checkbutton(self.app_frame, text='Egg Rolls', bg="yellow", variable=self.egg_rolls_var)
        self.edamame = tkinter.Checkbutton(self.app_frame, text='Edamame', bg="yellow", variable=self.edamame_var)
        self.yakitori = tkinter.Checkbutton(self.app_frame, text='Yakitori', bg="yellow", variable=self.yakitori_var)

        self.app_label.pack()
        self.gyoza.pack(side="left")
        self.house_salad.pack(side="left")
        self.egg_rolls.pack(side="left")
        self.edamame.pack(side="left")
        self.yakitori.pack(side="left")


# drinks and checkbox variables
        self.water_var = tkinter.IntVar()
        self.green_tea_var = tkinter.IntVar()
        self.hot_tea_var = tkinter.IntVar()
        self.coke_var = tkinter.IntVar()
        self.sapporo_var = tkinter.IntVar()
        self.miller_var = tkinter.IntVar()
        self.hot_sake_var = tkinter.IntVar()
        self.sake_var = tkinter.IntVar()

        self.water_var.set(0)
        self.green_tea_var.set(0)
        self.hot_tea_var.set(0)
        self.coke_var.set(0)
        self.sapporo_var.set(0)
        self.miller_var.set(0)
        self.hot_sake_var.set(0)
        self.sake_var.set(0)

        self.drink_label = tkinter.Label(self.drink_frame, text="Drinks", bg="yellow", fg="blue", font="Calibri 16 bold")
        self.water = tkinter.Checkbutton(self.drink_frame, text='Water', bg="yellow", variable=self.water_var)
        self.green_tea = tkinter.Checkbutton(self.drink_frame, text='Green Tea', bg="yellow", variable=self.green_tea_var)
        self.hot_tea = tkinter.Checkbutton(self.drink_frame, text='Hot Tea', bg="yellow", variable=self.hot_tea_var)
        self.coke = tkinter.Checkbutton(self.drink_frame, text='Coca Cola', bg="yellow", variable=self.coke_var)
        self.sapporo = tkinter.Checkbutton(self.drink_frame, text='Sapporo', bg="yellow", variable=self.sapporo_var)
        self.miller = tkinter.Checkbutton(self.drink_frame, text='Miller Lite', bg="yellow", variable=self.miller_var)
        self.hot_sake = tkinter.Checkbutton(self.drink_frame, text="Hot Sake", bg="yellow", variable=self.hot_sake_var)
        self.sake = tkinter.Checkbutton(self.drink_frame, text="Sake", bg="yellow", variable=self.sake_var)

        self.drink_label.pack()
        self.water.pack(side="left")
        self.green_tea.pack(side="left")
        self.hot_tea.pack(side="left")
        self.coke.pack(side='left')
        self.sapporo.pack(side='left')
        self.miller.pack(side='left')
        self.hot_sake.pack(side='left')
        self.sake.pack(side='left')

        # variable for radiobutton widget
        self.ramen_var = tkinter.IntVar()
        self.size_var = tkinter.IntVar()

        # initialize radio button widgets
        self.ramen_var.set(1)
        self.size_var.set(1)

        self.ramen_label = tkinter.Label(self.ramen_frame, text='Ramen', bg="yellow", fg="blue", font="Calibri 16 bold")
        self.broth1 = tkinter.Radiobutton(self.ramen_frame, text='Shio (Salt) Broth', bg="yellow", variable=self.ramen_var, value=1)
        self.broth2 = tkinter.Radiobutton(self.ramen_frame, text='Tonkotsu (Pork) Broth', bg="yellow", variable=self.ramen_var, value=2)
        self.broth3 = tkinter.Radiobutton(self.ramen_frame, text='Miso (Soybean) Broth', bg="yellow", variable=self.ramen_var, value=3)
        self.broth4 = tkinter.Radiobutton(self.ramen_frame, text='Shoyu (Soy Sauce) Broth', bg="yellow", variable=self.ramen_var, value=3)

        self.ramen_label.pack()
        self.broth1.pack(side="left")
        self.broth2.pack(side="left")
        self.broth3.pack(side="left")
        self.broth4.pack(side='left')

        self.size_label = tkinter.Label(self.size_frame, text='Size', bg="yellow", fg="blue", font="Calibri 16 bold")
        self.size1 = tkinter.Radiobutton(self.size_frame, text='Small - $7.25', bg="yellow", variable=self.size_var, value=1)
        self.size2 = tkinter.Radiobutton(self.size_frame, text='Medium - $8.25', bg="yellow", variable=self.size_var, value=2)
        self.size3 = tkinter.Radiobutton(self.size_frame, text='Large - $10.00', bg="yellow", variable=self.size_var, value=3)

        self.size_label.pack()
        self.size1.pack(side="left")
        self.size2.pack(side="left")
        self.size3.pack(side="left")

        # add ins and checkbox variables
        self.chashu_var = tkinter.IntVar()
        self.mushrooms_var = tkinter.IntVar()
        self.egg_var = tkinter.IntVar()
        self.bamboo_var = tkinter.IntVar()
        self.negi_var = tkinter.IntVar()
        self.moyashi_var = tkinter.IntVar()
        self.naruto_var = tkinter.IntVar()

        self.chashu_var.set(0)
        self.mushrooms_var.set(0)
        self.egg_var.set(0)
        self.bamboo_var.set(0)
        self.negi_var.set(0)
        self.moyashi_var.set(0)
        self.naruto_var.set(0)

        self.add_label = tkinter.Label(self.add_ons_frame, text="Add Ons", bg="yellow", fg="blue", font="Calibri 16 bold")
        self.chashu = tkinter.Checkbutton(self.add_ons_frame, text='Chashu', bg="yellow", variable=self.chashu_var)
        self.mushrooms = tkinter.Checkbutton(self.add_ons_frame, text='Mushrooms', bg="yellow", variable=self.mushrooms_var)
        self.egg = tkinter.Checkbutton(self.add_ons_frame, text='Egg', bg="yellow", variable=self.egg_var)
        self.bamboo_shoots = tkinter.Checkbutton(self.add_ons_frame, text='Bamboo Shoots', bg="yellow", variable=self.bamboo_var)
        self.negi = tkinter.Checkbutton(self.add_ons_frame, text='Negi (Green Onions/Leeks)', bg="yellow", variable=self.negi_var)
        self.moyashi = tkinter.Checkbutton(self.add_ons_frame, text='Moyashi (Bean Sprouts)', bg="yellow", variable=self.moyashi_var)
        self.naruto = tkinter.Checkbutton(self.add_ons_frame, text="Naruto (Fish Cake)", bg="yellow", variable=self.naruto_var)

        self.add_label.pack()
        self.chashu.pack(side="left")
        self.mushrooms.pack(side="left")
        self.egg.pack(side="left")
        self.bamboo_shoots.pack(side='left')
        self.negi.pack(side='left')
        self.moyashi.pack(side='left')
        self.naruto.pack(side='left')
        # order

        self.order_button = tkinter.Button(self.order_frame, text='Order', bg="green", fg="blue", font="Calibri 16 bold", command=self.display)
        self.cancel_button = tkinter.Button(self.order_frame, text='Cancel', bg="red", fg="blue", font="Calibri 16 bold", command=self.main_window.destroy)

        self.order_button.pack(side='left')
        self.cancel_button.pack(side='left')
        # charges
        self.order_info = tkinter.StringVar()
        self.order_output = tkinter.Label(self.charges_frame, textvariable=self.order_info)
        self.order_output.pack()

        # pack frames
        self.drink_frame.pack()
        self.app_frame.pack()
        self.ramen_frame.pack()
        self.size_frame.pack()
        self.add_ons_frame.pack()
        self.order_frame.pack()
        self.charges_frame.pack()

        tkinter.mainloop()

    def display(self):
        output = "you ordered a ",
        if self.water_var.get() == 1:
            output += "water "
        if self.green_tea_var.get() == 1:
            output += "Green Tea "
        if self.hot_tea_var.get() == 1:
            output += "Hot Tea "
        if self.coke_var.get() == 1:
            output += "Coca Cola  "
        if self.sapporo_var.get() == 1:
            output += "Sapporo  "
        if self.miller_var.get() == 1:
            output += "Miller Lite "
        if self.hot_sake_var.get() == 1:
            output += "Hot Sake "
        if self.sake_var.get() == 1:
            output += "Sake "

        if self.gyoza_var.get() == 1:
            output += ", a side of Gyoza, "
        if self.house_salad_var.get() == 1:
            output += ", a side of House Salad, "
        if self.egg_rolls_var.get() == 1:
            output += ", a side of Egg Rolls, "
        if self.edamame_var.get() == 1:
            output += ", a side of Edamame, "
        if self.yakitori_var.get() == 1:
            output += ", a side of Yakitori, "

        if self.size_var.get() == 1:
            output += "a small "
        elif self.size_var.get() == 2:
            output += "a Medium "
        elif self.size_var.get() == 3:
            output += "a Large "

        if self.ramen_var.get() == 1:
            output += "Shio Broth"
        elif self.ramen_var.get() == 2:
            output += "Tonkotsu Broth"
        elif self.ramen_var.get() == 3:
            output += "Miso Broth"
        elif self.ramen_var.get() == 4:
            output += "Shoyu Broth"

        if self.size_var.get() == 1:
            output += " for $7.25 "
        elif self.size_var.get() == 2:
            output += " for $8.25 "
        elif self.size_var.get() == 3:
            output += " for $10.00 "

        if self.chashu_var.get() == 1:
            output += "\nwith Chashu "
        if self.mushrooms_var.get() == 1:
            output += "\nwith Mushrooms "
        if self.egg_var.get() == 1:
            output += "\nwith Egg "
        if self.bamboo_var.get() == 1:
            output += "\nwith Bamboo Shoots "
        if self.negi_var.get() == 1:
            output += "\nwith Negi (Green Onions) "
        if self.moyashi_var.get() == 1:
            output += "\nwith Moyashi (Bean Sprouts) "
        if self.naruto_var.get() == 1:
            output += "\nwith Naruto (Fish Cake) "
        self.order_info.set(output)


noodle = Ramen()
