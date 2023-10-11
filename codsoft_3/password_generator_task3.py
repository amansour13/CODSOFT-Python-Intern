"""
Task 1       : Password Generator
Author       : Ahmed Mansour
Version      : v0.1
Release Date : 6/10/2023

Description:
This Password Generator App is just a app that generates a strong password according to the length user entered.

Contact Information:
If you have any questions, suggestions, or feedback, feel free to reach out to the author:
- Email: a.mansour1345@gmail.com
"""

import random
import string
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import pyperclip
first_color, second_color, third_color, forth_color = "#161616", "#346751", "#C84B31", "#ECDBBA"


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

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def generate_password(length):
    charset = string.ascii_letters + string.digits + "!@#$%^&*()_+~}{[]:;?><,./-="
    password = ""
    has_upper, has_lower, has_num, has_sym = False, False, False, False

    for i in range(length):
        random_index = random.randint(0, len(charset) - 1)
        random_char = charset[random_index]

        if random_char.islower():
            has_lower = True
        elif random_char.isupper():
            has_upper = True
        elif random_char.isdigit():
            has_num = True
        else:
            has_sym = True

        password += random_char

    if not (has_lower and has_upper and has_num and has_sym):
        return generate_password(length)
    else:
        return password

def handle_generate_password_btn():
    current_len = pass_len_ent.get()
    if (not current_len.isdigit()):
        messagebox.showinfo("Invalid Length", "please enter a valid number (not decimal or any other chars) :)")
    elif (int(current_len) <= 5):
        messagebox.showinfo("Invalid Lenght", "password length cannot be smaller than or equal 5 :)")
    else:
        password = generate_password(int(current_len))
        gen_pass_ent.config(state='normal')
        gen_pass_ent.delete(0, END)
        gen_pass_ent.insert(END, password)
        gen_pass_ent.config(state="disabled")

def handle_reject_btn():
    gen_pass_ent.config(state='normal')
    gen_pass_ent.delete(0, END)
    gen_pass_ent.config(state="disabled")

def handle_accept_btn():
    accepted_password = gen_pass_ent.get()
    try: 
        pyperclip.copy(accepted_password)
    except Exception as e:
        messagebox.showwarning("Copy to Clipboard", "Your Password could not copied to clipboard")
    else:
        messagebox.showinfo("Copy to Clipboard", "Your Password copied to clipboard successfully")

# initialize the form
main = tk.Tk()
main.title("Password Generator")
# main.resizable(False, False)
main.config(bg=first_color)
center_window(main, 600, 500)

# set upper_section or title's section
upper_section = PanedWindow(bg=second_color, height=1)
upper_section.pack(side='top', fill=BOTH)
title = Label(upper_section, text="Password Generator", bg=second_color, fg=forth_color, font=('Helvetica', 25, 'bold'))
title.pack(side="left", anchor='w', fill='both', expand=True, pady=20)

# add row frames to the screen
first_row = Frame(main, bg=first_color, pady=10, padx=10)
first_row.pack(side='top', anchor='w',fill="both", pady=20)

pass_len_lbl = Label(first_row, anchor='w', text="Enter Password Length:", bg=first_color, fg=forth_color, font=('Helvetica', 14))
pass_len_lbl.pack(side="left", anchor='w', fill='both', expand=True)

pass_len_ent = Entry(first_row, font=('Helvetica', 14, "bold"), relief="flat", fg=first_color)
pass_len_ent.pack(side='left',anchor="w", fill="both", expand=True)


second_row = Frame(main, bg=first_color, pady=10, padx=10)
second_row.pack(side='top', anchor='w',fill="both", pady=20)

gen_pass_lbl = Label(second_row, text="Generated Password:   ", anchor='w', bg=first_color, fg=forth_color, font=('Helvetica', 14))
gen_pass_lbl.pack(side="left", anchor='w', fill='both', expand=True)

gen_pass_ent = Entry(second_row, font=('Helvetica', 14, "bold"), relief="flat", fg=forth_color,  state='readonly')
gen_pass_ent.pack(side='left',anchor="w", fill="both", expand=True)


gen_btn = HoverButton(main, text='Generate Password', relief="flat", font=('Helvetica', 15), padx= 10, bg=second_color, fg=third_color, activebackground=third_color, activeforeground=second_color)
gen_btn.pack(side='top', padx=10, pady=20, anchor="n")
gen_btn.config(command=handle_generate_password_btn)

acc_btn = HoverButton(main, text='Accept', relief="solid", font=('Helvetica', 15), padx= 10, bg=first_color, fg=third_color, activebackground=third_color, activeforeground=second_color, highlightthickness=5, highlightbackground='red')
acc_btn.pack(side='top', padx=10, pady=10, anchor="n")
acc_btn.config(command=handle_accept_btn)

rej_btn = HoverButton(main, text='Reject', relief="solid", font=('Helvetica', 15), padx= 10, bg=first_color, fg=third_color, activebackground=third_color, activeforeground=second_color, highlightthickness=5, highlightbackground='red')
rej_btn.pack(side='top', padx=10, pady=10, anchor="n")
rej_btn.config(command=handle_reject_btn)

main.mainloop()
