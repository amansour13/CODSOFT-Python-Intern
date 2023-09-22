from tkinter import *

import tkinter as tk
first_color, second_color, third_color, forth_color = "#2C3333", "#2E4F4F", "#0E8388", "#CBE4DE"


#functions or classes used in the program
class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.defaultForeground = self["foreground"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']
        self['foreground'] = self['activeforeground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground
        self['foreground'] = self.defaultForeground

# initialize the form
main = tk.Tk()
main.title("ToDo List App")
main.geometry("1000x600")

# set upper_section or title's section
upper_section = PanedWindow(bg=second_color, height=1)
upper_section.pack(fill=BOTH, expand=1)
title = Label(upper_section, text="TO-DO List", bg=second_color, fg=forth_color, font=('Helvetica', 25, 'bold'))
upper_section.add(title)

# Create a frame for the main content
main_frame = Frame(main, bg=first_color, padx=50)
main_frame.pack(fill=BOTH, expand=1)

add_item_title = Label(main_frame, text="Add Items", bg=first_color, fg=forth_color, font=('Helvetica', 20, 'bold'), pady=30)
add_item_title.grid(row=0, column=0, sticky="nw")

new_task_en = Entry(main_frame, width=70, font=('Helvetica', 15), relief="flat", fg=second_color)
new_task_en.grid(row=1, column=0, sticky="w")

submit_btn = HoverButton(main_frame, text="submit", relief="flat", padx=10, bg=third_color, fg=forth_color, activebackground=forth_color, activeforeground=second_color)
submit_btn.grid(row=1, column=1, sticky="w", padx=10)

tasks_title = Label(main_frame, text="Tasks", bg=first_color, fg=forth_color, font=('Helvetica', 20, 'bold'), pady=30)
tasks_title.grid(row=2, column=0, sticky="nw")


# ready to run the application after set all widgets
main.mainloop()

