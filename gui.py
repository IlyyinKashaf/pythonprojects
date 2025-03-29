from tkinter import *

# Initialize the screen
screen = Tk()
screen.title("Miles to Kilometer Converter")
screen.minsize(width= 300 , height = 100)
screen.config(padx = 40 , pady= 20)

def miles_to_km ():
    miles = float(miles_input.get())
    km = miles * 1.609
    result_label.config(text = f"{km}")

miles_input = Entry(width = 10)
miles_input.grid(column = 1, row = 1)

miles_label = Label(text = "Miles")
miles_label.grid(column = 2 , row = 1)

km_label = Label (text = 'Km')
km_label.grid(column = 2 , row = 2)

is_equal = Label(text = 'is equal to')
is_equal.grid(column = 0 , row = 2)


result_label = Label (text = '0')
result_label.grid(column = 1 , row = 2)

calculate_button = Button(text = 'Calculate', command = miles_to_km)
calculate_button.grid(column = 1 , row = 4)





# Run the main event loop
screen.mainloop()
