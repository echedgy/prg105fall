# Make up an interface for a business offering 7-10 services or product options with prices.
# Write a GUI program to allow the user to click buttons to add services or products and show total at the bottom.
# Make sure all necessary labels and instructions to the user are included in your GUI.
# Provide options using data fields, radio buttons, or check boxes.

import tkinter


class Ramen:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.ramen_frame = tkinter.Frame(self.main_window)
        self.size_frame = tkinter.Frame(self.main_window)
        self.add_ons_frame = tkinter.Frame(self.main_window)
        self.order_frame = tkinter.Frame(self.main_window)
        self.charges_frame = tkinter.Frame(self.main_window)

        # variable for radiobutton widget
        self.ramen_var = tkinter.IntVar()
        self.size_var = tkinter.IntVar()

        # initialize radio button widgets
        self.ramen_var.set(1)
        self.size_var.set(1)

        self.ramen_label = tkinter.Label(self.ramen_frame, text='Ramen')
        self.broth1 = tkinter.Radiobutton(self.ramen_frame, text='Salt Broth', variable=self.ramen_var, value=1)
        self.broth2 = tkinter.Radiobutton(self.ramen_frame, text='Pork Broth', variable=self.ramen_var, value=2)
        self.broth3 = tkinter.Radiobutton(self.ramen_frame, text='Veggie Broth', variable=self.ramen_var, value=3)

        self.ramen_label.pack()
        self.broth1.pack(side="left")
        self.broth2.pack(side="left")
        self.broth3.pack(side="left")

        self.size_label = tkinter.Label(self.size_frame, text='Size')
        self.size1 = tkinter.Radiobutton(self.size_frame, text='Small - $7.25', variable=self.size_var, value=1)
        self.size2 = tkinter.Radiobutton(self.size_frame, text='Medium - $8.25', variable=self.size_var, value=2)
        self.size3 = tkinter.Radiobutton(self.size_frame, text='Large - $10.00', variable=self.size_var, value=3)

        self.size_label.pack()
        self.size1.pack(side="left")
        self.size2.pack(side="left")
        self.size3.pack(side="left")

        # add ins and checkbox variables
        self.chashu_var = tkinter.IntVar()
        self.mushrooms_var = tkinter.IntVar()
        self.egg_var = tkinter.IntVar()

        self.chashu_var.set(0)
        self.mushrooms_var.set(0)
        self.egg_var.set(0)

        self.add_label = tkinter.Label(self.add_ons_frame, text="Add Ons")
        self.chashu = tkinter.Checkbutton(self.add_ons_frame, text='Chashu', variable=self.chashu_var)
        self.mushrooms = tkinter.Checkbutton(self.add_ons_frame, text='Mushrooms', variable=self.mushrooms_var)
        self.egg = tkinter.Checkbutton(self.add_ons_frame, text='Egg', variable=self.egg_var)

        self.add_label.pack()
        self.chashu.pack(side="left")
        self.mushrooms.pack(side="left")
        self.egg.pack(side="left")

        # order

        self.order_button = tkinter.Button(self.order_frame, text='Order', command=self.display)
        self.cancel_button = tkinter.Button(self.order_frame, text='Cancel', command=self.main_window.destroy)

        self.order_button.pack(side='left')
        self.cancel_button.pack(side='left')
        # charges
        self.order_info = tkinter.StringVar()
        self.order_output = tkinter.Label(self.charges_frame, textvarable=self.order_info)
        self.order_output.pack()

        # pack frames
        self.ramen_frame.pack()
        self.size_frame.pack()
        self.add_ons_frame.pack()
        self.order_frame.pack()
        self.charges_frame.pack()

        tkinter.mainloop()

    def display(self):
        output = "you ordered a "
        if self.size_var.get() == 1:
            output += " a small "
        elif self.size_var.get() == 2:
            output += " a Medium "
        elif self.size_var.get() == 3:
            output += " a Large "

        if self.ramen_var.get() == 1:
            output += "Salt Broth"
        elif self.ramen_var.get() == 2:
            output += "Pork Broth"
        elif self.ramen_var.get() == 3:
            output += "Veggie Broth"

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

        self.order_info.set(output)


ramen = Ramen()
