"""
Task 1       : To-Do List App
Author       : Ahmed Mansour
Version      : v0.2
Release Date : 2/10/2023

Description:
This To-Do List App is a simple task management tool that allows users to create, edit, and delete tasks. It provides an easy way to organize your tasks and keep track of your to-do items.

Contact Information:
If you have any questions, suggestions, or feedback, feel free to reach out to the author:
- Email: a.mansour1345@gmail.com
"""

from tkinter import *

import tkinter as tk
from tkinter import ttk
import json
first_color, second_color, third_color, forth_color = "#2C3333", "#2E4F4F", "#0E8388", "#CBE4DE"

try: 
    file = open("tasks.json", 'r')
    tasks = json.load(file)
    file.close()
except FileNotFoundError:
    print ("please check for the path of the Database (JSON) file")
    tasks = []
except:
    print("an Error occured")
else:
    print ("DB file opened succesfully :)")

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
        self.task_frame.pack(side="top", fill='both',padx=5, pady=5)
        self.task_label = Label(self.task_frame, wraplength=750, anchor="w", text=task_text, bg=third_color, fg=second_color, font=('Helvetica', 15), pady=5, width=68)
        self.task_label.pack(side="left")

        self.delete_button = HoverButton(self.task_frame, text="delete", relief="flat", padx=10, bg='darkred', fg=forth_color, activebackground=forth_color, activeforeground=second_color, pady=5)
        self.delete_button.pack(side='right')
        self.delete_button.config(command=self.delete)

        self.edit_button = HoverButton(self.task_frame, text="edit", relief="flat", padx=10, bg='darkgreen', fg=forth_color, activebackground=forth_color, activeforeground=second_color, pady=5)
        self.edit_button.pack(side='right', padx=5)
        self.edit_button.config(command=self.edit)

        
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
                i.task_frame.pack_forget()
                all_tasks.remove(i)
                message.config(text="task deleted succesfully :)", fg="red")
                break
    def __del__(self):
        TaskWidget.ctr_tasks -= 1

def add_new_task():
    message.config(text="", fg='lightgreen')
    task_txt = new_task_en.get()
    all_tasks.append(TaskWidget(scrollable_content_frame, task_txt))
    new_task_en.delete(0, END)
    
def edit_task():
    all_tasks[edit_task_index].change_task_text(new_task_en.get())
    new_task_en.delete(0, END)
    submit_btn.config(text="submit")
    message.config(text="Task edited succesfully :)", fg="lightgreen")

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

def old_tasks():
    for i in tasks:
        all_tasks.append(TaskWidget(scrollable_content_frame, i))



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

add_item_title = Label(main_frame, text="Add Items", bg=first_color, fg=forth_color, font=('Helvetica', 20, 'bold'), pady=10)
add_item_title.pack(side='top', anchor='w')

message = Label(main_frame, text="", bg=first_color, fg="lightgreen", font=('Helvetica', 8, 'bold'), pady=2)
message.pack(side='top', anchor='w')

entry_button_frame = Frame(main_frame, bg=first_color)
entry_button_frame.pack(side='top', anchor='w')

new_task_en = Entry(entry_button_frame, width=70, font=('Helvetica', 15), relief="flat", fg=second_color)
new_task_en.pack(side='left', padx=5, pady=5, anchor="w")

submit_btn = HoverButton(entry_button_frame, text="submit", relief="flat", padx=10, bg=third_color, fg=forth_color, activebackground=forth_color, activeforeground=second_color)
submit_btn.pack(side='left', padx=10)
submit_btn.config(command=btn_functions)

tasks_title = Label(main_frame, text="Tasks", bg=first_color, fg=forth_color, font=('Helvetica', 20, 'bold'), pady=20)
tasks_title.pack(side='top', anchor='w')


test = Frame(main_frame)
test.pack(side="top", fill="x")

# Create a canvas widget inside the scrollable_frame
canvas = tk.Canvas(test, bg=first_color, relief='flat', highlightthickness=0)
canvas.pack(fill="both", expand=True, side="left")

# Create a vertical scrollbar for the canvas
scrollbar = ttk.Scrollbar(test, orient="vertical", command=canvas.yview)
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

scrollable_content_frame.bind("<Configure>", configure_scrollable_frame)

# Create a frame to contain additional content below the scrollbar
space_frame = Frame(main_frame, bg=first_color, pady=0)
space_frame.pack(side="bottom", anchor="w")

old_tasks()
tasks = []
# ready to run the application after set all widgets
main.mainloop()

for i in all_tasks:
    tasks.append(i.get_task_text())



try: 
    file = open("tasks.json", "w")
    json.dump(tasks, file, indent=2)
    file.close()
except FileNotFoundError:
    print ("please check for the path of the Database (JSON) file")
    print ("Data save failed :(")
except:
    print("an Error occured")
else:
    print ("Data saved succesfully in DB :)")
