from tkinter import *

import tkinter as tk
first_color, second_color, third_color, forth_color = "#2C3333", "#2E4F4F", "#0E8388", "#CBE4DE"

# initialize the form
main = tk.Tk()
main.title("ToDo List App")
main.geometry("1000x600")

# set upper_section or title's section
upper_section = PanedWindow(bg=second_color, height=200)
upper_section.pack(fill=BOTH, expand=1)
title = Label(upper_section, text="TODO List", bg=second_color, fg=forth_color, font=('Helvetica', 25, 'bold'))
upper_section.add(title)

# set main section
main_section = PanedWindow(bg=first_color,height=400)
main_section.pack(fill=BOTH, expand=1)
add_item_title = Label(main_section, text="Add Items",bg=first_color, fg=forth_color, font=('Helvetica', 20, 'bold'), pady=50, padx=50)
main_section.add(add_item_title)

# align text to the top left corner
add_item_title.pack(side=LEFT, anchor=NW)

# ready to run the application after set all widgets
main.mainloop()