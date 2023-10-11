"""
Task 1       : Calculator
Author       : Ahmed Mansour
Version      : v0.1
Release Date : 6/10/2023

Description:
This Calculator App is a simple calculator that calculate the basic operations using python tkinter lib as GUI.

Contact Information:
If you have any questions, suggestions, or feedback, feel free to reach out to the author:
- Email: a.mansour1345@gmail.com
"""


from tkinter import *
import tkinter as tk
import math as math
from tkinter import messagebox

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

def btn_func(txt):
    if (txt == "CE"):
        current_text = output.get()
        if current_text:
            output.config(state='normal')
            new_text = current_text[:-1]
            output.delete(0, END)
            output.insert(END, new_text)
            output.config(state="disabled")
    if (txt == "C"):
        current_text = output.get()
        if current_text:
            output.config(state='normal')
            output.delete(0, END)
            output.config(state="disabled")
    if ("0" <= txt <= "9" or txt in ['+', '-', '/', '*', '.']):
        output.config(state="normal")
        output.insert(END, txt)
        output.config(state="disabled")
    if (txt == '='):
        current_text = output.get()
        if current_text:
            try:
                new_text = eval(current_text)
            except Exception as e:
                messagebox.showinfo("Invalid equation:", e)
                new_text = current_text
            output.config(state='normal')
            output.delete(0, END)
            output.insert(END, new_text)
            output.config(state="disabled")
        else:
            output.config(state='normal')
            output.insert(END, '0')
            output.config(state="disabled")
    if (txt == '√'):
        current_text = output.get()
        if current_text:
            try:
                new_text = eval(current_text)
                new_text = eval(str(math.sqrt(new_text)))
            except Exception as e:
                messagebox.showinfo("Invalid equation:", e)
                new_text = current_text
            output.config(state='normal')
            output.delete(0, END)
            output.insert(END, new_text)
            output.config(state="disabled")
        else:
            output.config(state='normal')
            output.insert(END, '0')
            output.config(state="disabled")
    if (txt == '!'):
        current_text = output.get()
        if current_text:
            try:
                new_text = eval(current_text)
                new_text = eval(str(math.factorial(new_text)))
            except Exception as e:
                messagebox.showinfo("Invalid equation:", e)
                new_text = current_text
            output.config(state='normal')
            output.delete(0, END)
            output.insert(END, new_text)
            output.config(state="disabled")
        else:
            output.config(state='normal')
            output.insert(END, '1')
            output.config(state="disabled")
    


btns = ["C", "√", "/", "CE",
        "7", "8", "9", "*",
        "4", "5", "6", "-",
        "1", "2", "3", "+",
        "!", "0", ".", "="]


# initialize the form
main = tk.Tk()
main.title("Simple Calculator")
# main.resizable(False, False)
main.config(bg=forth_color)
center_window(main, 400, 400)

# add frame to hold the entry of the output
entry_frame = Frame(main, bg=first_color, pady=10, padx=10)
entry_frame.pack(side='top', anchor='w',fill="both")

# add the output screen or entry to its frame
output = Entry(entry_frame, font=('Helvetica', 15, "bold"), relief="flat", fg=third_color, bg=forth_color, state="disabled")
output.pack(side='left', padx=5, pady=5, anchor="w", fill="both", expand=True)

# add row frames to the screen
first_row = Frame(main, bg=first_color, pady=10, padx=10)
first_row.pack(side='top', anchor='w',fill="both")

second_row = Frame(main, bg=first_color, pady=10, padx=10)
second_row.pack(side='top', anchor='w',fill="both")

third_row = Frame(main, bg=first_color, pady=10, padx=10)
third_row.pack(side='top', anchor='w',fill="both")

forth_row = Frame(main, bg=first_color, pady=10, padx=10)
forth_row.pack(side='top', anchor='w',fill="both")

fifth_row = Frame(main, bg=first_color, pady=10, padx=10)
fifth_row.pack(side='top', anchor='w',fill="both")

# reload all buttons on the screen
for i in range(len(btns)):
    if   (i < 4):
        temp = first_row
    elif (i < 8):
        temp = second_row
    elif (i < 12):
        temp = third_row
    elif (i < 16):
        temp = forth_row
    else:
        temp = fifth_row
    
    btn = HoverButton(temp, text=btns[i], relief="flat", font=('Helvetica', 15), padx= 10 if btns[i] != "CE" else 3, bg=second_color, fg=third_color, activebackground=third_color, activeforeground=second_color)
    btn.pack(side='left', padx=10, pady=5, anchor="w", fill="both", expand=True)
    btn.config(command=lambda txt=btns[i]: btn_func(txt))



# ready to run the application after set all widgets
main.mainloop()