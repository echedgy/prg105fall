# Write a GUI program that displays your name and address when a button is clicked (you can use the address of the school).
# The program’s window should resemble the sketch on the far left side of figure 13-26 when it runs.
# When the user clicks the Show Info button, the program should display your name and address as shown in the sketch on the right of the figure.

import tkinter


class MyGui:
    def __init__(self):  # create the main window

        self.main_window = tkinter.Tk()
# create StringVar objects to display name
# street, and city-state-zip
        self.name_value = tkinter.StringVar()
        self.street_value - tkinter.StringVar()
        self.csz_value = tkinter.StringVar()
# create two frames
        self.info_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)
# create the label widgets, associated with the StringVar objects.
        self.name_label = tkinter.Label(self.info_frame, textvariable=self.name_value)
        self.street_label = tkinter.Label(self.info_frame, textvariable=self.street_value)
        self.csz_label = tkinter.Label(self.info_frame, textvariable=self.csz_value)
# pack the label
        self.name_label.pack()
        self.street_label.pack()
        self.csz_label.pack()

# create the button widgets
        self.show_info_button = tkinter.Button(self.button_frame, text='Show Info', command=self.show)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)

# pack the buttons
        self.show_info_button.pack(side='left')
        self.quit_button.pack(side='right')

# pack the frames
        self.info_frame.pack()
        self.button_frame.pack()

# enter the tkinter main loop
        tkinter.mainloop()
# callback function for the Show Info button
    def show(self):
        self.name_value.set('Eric Chedgy')
        self.street_value.set('4713 Southhampton Dr.')
        self.csz_value.set('Island Lake, Illinois 60042')

my_gui = MyGui()
