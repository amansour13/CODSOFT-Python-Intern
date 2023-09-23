"""
Task 1       : To-Do List App
Author       : Ahmed Mansour
Version      : v0.1
Release Date : 23/9/2023

Description:
This To-Do List App is a simple task management tool that allows users to create, edit, and delete tasks. It provides an easy way to organize your tasks and keep track of your to-do items.

Contact Information:
If you have any questions, suggestions, or feedback, feel free to reach out to the author:
- Email: a.mansour1345@gmail.com
"""

from tkinter import *

import tkinter as tk
from tkinter import ttk
first_color, second_color, third_color, forth_color = "#2C3333", "#2E4F4F", "#0E8388", "#CBE4DE"

# list of all tasks
all_tasks = []

# the current task user choose to edit 
# for value -1 this means there is no task to edit still 
edit_task_index = -1


#functions or classes used in the program

# hoverbutton class to add the hover effect to button widget
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

# taskwidgt class that is responsible for each new task section
class TaskWidget:
    ctr_tasks = 0
    txt = ""
    def __init__(self, parent_frame, task_text):
        self.task_frame = Frame(parent_frame, bg=third_color, height=60, highlightbackground=forth_color, highlightthickness=1)
        self.task_frame.grid(row=self.ctr_tasks + 4, column=0, columnspan=3 , sticky="w", pady=5)
        self.task_label = Label(self.task_frame, wraplength=750, anchor="w", text=task_text, bg=third_color, fg=second_color, font=('Helvetica', 15), pady=5, width=68)
        self.task_label.grid(row=0, column=0, sticky=W)

        self.edit_button = HoverButton(self.task_frame, text="edit", relief="flat", padx=10, bg='darkgreen', fg=forth_color, activebackground=forth_color, activeforeground=second_color, pady=5)
        self.edit_button.grid(row=0, column=1, sticky=E, padx=5)
        self.edit_button.config(command=self.edit)

        self.delete_button = HoverButton(self.task_frame, text="delete", relief="flat", padx=10, bg='darkred', fg=forth_color, activebackground=forth_color, activeforeground=second_color, pady=5)
        self.delete_button.grid(row=0, column=2, sticky=E)
        self.delete_button.config(command=self.delete)
        TaskWidget.ctr_tasks += 1
        self.txt = task_text

    def get_task_text(self):
        return self.txt
    
    def edit(self):
        new_task_en.delete(0, END)
        new_task_en.insert(0, self.txt)
        global edit_task_index
        edit_task_index = all_tasks.index(self)
        submit_btn.config(text="EDIT")
    
    def change_task_text(self, new_text):
        self.txt = new_text
        self.task_label.config(text=new_text)

    def delete(self):
        for i in all_tasks:
            if (i.get_task_text() == self.txt):
                i.task_frame.grid_remove()
                all_tasks.remove(i)
                break
    def __del__(self):
        TaskWidget.ctr_tasks -= 1

def add_new_task():
    task_txt = new_task_en.get()
    all_tasks.append(TaskWidget(scrollable_content_frame, task_txt))
    new_task_en.delete(0, END)
    
def edit_task():
    all_tasks[edit_task_index].change_task_text(new_task_en.get())
    new_task_en.delete(0, END)
    submit_btn.config(text="submit")

def btn_functions():
    if (submit_btn.cget("text") == "submit"):
        add_new_task()
    else:
        edit_task()

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

# initialize the form
main = tk.Tk()
main.title("ToDo List App")
main.resizable(False, False)
center_window(main, 1000, 600)

# set upper_section or title's section
upper_section = PanedWindow(bg=second_color, height=1)
upper_section.pack(fill=BOTH, expand=0)
title = Label(upper_section, text="TO-DO List", anchor="n", bg=second_color, fg=forth_color, font=('Helvetica', 25, 'bold'))
title.grid(row=0, column=0, padx=400, pady=20)

# Create a frame for the main content
main_frame = Frame(main, bg=first_color, padx=50)
main_frame.pack(fill=BOTH, expand=1)

add_item_title = Label(main_frame, text="Add Items", bg=first_color, fg=forth_color, font=('Helvetica', 20, 'bold'), pady=30)
add_item_title.grid(row=0, column=0, sticky="nw")

new_task_en = Entry(main_frame, width=70, font=('Helvetica', 15), relief="flat", fg=second_color)
new_task_en.grid(row=1, column=0, sticky="w")

submit_btn = HoverButton(main_frame, text="submit", relief="flat", padx=10, bg=third_color, fg=forth_color, activebackground=forth_color, activeforeground=second_color)
submit_btn.grid(row=1, column=1, sticky="w", padx=10)
submit_btn.config(command=btn_functions)

tasks_title = Label(main_frame, text="Tasks", bg=first_color, fg=forth_color, font=('Helvetica', 20, 'bold'), pady=20)
tasks_title.grid(row=2, column=0, sticky="nw")

# Create a frame to contain the scrollable content inside main_frame
scrollable_frame = tk.Frame(main_frame)
scrollable_frame.grid(row=3, column=0, columnspan=2, sticky="ew")

# Configure the columns to expand horizontally
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)

# Create a canvas widget inside the scrollable_frame
canvas = tk.Canvas(scrollable_frame, bg=first_color, relief='flat', highlightthickness=0)
canvas.pack(fill="both", expand=True, side="left")

# Create a vertical scrollbar for the canvas
scrollbar = ttk.Scrollbar(scrollable_frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y", pady=0)
scrollbar['takefocus'] = 0
# Configure the canvas to work with the scrollbar
canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame to contain the scrollable content
scrollable_content_frame = tk.Frame(canvas, bg=first_color)
canvas.create_window((0, 0), window=scrollable_content_frame, anchor="nw")


def on_mousewheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

canvas.bind_all("<MouseWheel>", on_mousewheel)

# Update the canvas scroll region when the frame size changes
def configure_scrollable_frame(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", configure_scrollable_frame)

# ready to run the application after set all widgets
main.mainloop()

