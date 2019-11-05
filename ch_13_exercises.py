"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""
import tkinter
import tkinter.messagebox
# TODO 13.2 Using the tkinter Module
print("=" * 10, "Section 13.2 using tkinter", "=" * 10)
# Write the code from program 13-2 to display an empty window, no need
# to re-import tkinter. Use the class name MyGUI2
class MyGUI:
    def __init__(self):

        self.main_window =tkinter.Tk()
        tkinter.mainloop()

#my_gui = MyGUI()
# TODO 13.3 Adding a label widget
print("=" * 10, "Section 13.3 adding a label widget", "=" * 10)
# Add a label to MyGUI2 (above) that prints your first and last name; pack the label
# Create an instance of MyGUI2
class MyGui2:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.label = tkinter.Label(self.main_window, text="Hello world")
        self.label.pack()

        tkinter.mainloop()


#my_gui2 = MyGui2()
# TODO 13.4 Organizing Widgets with Frames
print("=" * 10, "Section 13.4 using frames", "=" * 10)
# Create a MyGUI3 class that creates a window with two frames
# In the top Frame add labels with your name and major
# In the bottom frame add labels with the classes you are taking this semester
# Create an instance of MyGUI3


class MyGui3:
    def __init__(self):
        self.main_window = tkinter.Tk()
        #create 2 frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        # label widgets
        self.label1 = tkinter.label(self.top_frame, text = 'Eric Chedgy')
        self.label2 = tkinter.label(self.top_frame, text = 'Instructional Design')
        # adding the labels to the top frame
        self.label1.pack(side='Top')
        self.label2.pack(side='Top')

        self.label3 = tkinter.label(self.bottom_frame, text = 'Programming logic')
        self.label4 = tkinter.label(self.bottom_frame, text = 'Graphic design')
        self.label5 = tkinter.label(self.bottom_frame, text = 'Comp Lit')

        self.label3.pack(side='Left')
        self.label4.pack(side='Left')
        self.label5.pack(side='Left')

        # pack frames
        self.top_frame.pack(side='left')
        self.bottom_frame.pack(side='left')

        tkinter.mainloop()

# my_gui3 =MyGui3()

# TODO 13.5 Button Widgets and info Dialog Boxes
print("=" * 10, "Section 13.5 button widgets and info dialogs", "=" * 10)
# Create a GUI that will tell a joke
# Use a button to show the punch line, which should appear in a dialog box
# Create an instance of the GUI


class MyGui4:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.joke = tkinter.Label(self.main_window, text='Why did the chicken cross the road')

        self.why = tkinter.Button(self.main_window, text = "Why?", command=self.punchline)

        self.joke.pack()
        self.why.pack()

        tkinter.mainloop()

    def punchline(self):
        tkinter.messagebox.showinfo('Response', "Because he was tired of this joke!")


#my_gui4 = MyGui4()
# TODO 13.6 getting input / 13.7 Using Labels as output fields
print("=" * 10, "Section 13.6-13.7 input and output using Entry and Label", "=" * 10)
# Using the program in 13.10 kilo converter as a sample,
# create a program to convert inches to centimeters

class InchesConverterGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.prompt_label = tkinter.Label(self.top_frame, text='Enter a distance in inches: ')
        self.inches_entry = tkinter.Entry(self.top_frame, width=10)

        self.prompt_label.pack(side='left')
        self.inches_entry.pack(side='left')

        self.calc_button = tkinter.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):

        inches = float(self.inches_entry.get())
        centimeters = inches * 2.54
        tkinter.messagebox.showinfo('Results', str(inches) + 'inches is equal to ' + str(centimeters) + ' inches')

inches_conv = InchesConverterGUI()

