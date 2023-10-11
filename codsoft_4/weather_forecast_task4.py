# # coding: utf-8
# import requests
# import json



"""
Task 4       : weather forecast App
Author       : Ahmed Mansour
Version      : v0.1
Release Date : 11/10/2023

Description:
This weather forecast App is a simple program that show the weather details of a specific city based on user input which is the city or its zipcode.

Contact Information:
If you have any questions, suggestions, or feedback, feel free to reach out to the author:
- Email: a.mansour1345@gmail.com
"""

from tkinter import *

import tkinter as tk
from tkinter import ttk
first_color, second_color, third_color, forth_color = "#B6FFFA", "#98E4FF", "#80B3FF", "#687EFF"


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

def search():
    pass
    # params = {
    #   'access_key': 'a718126fecd2f38fe9a9411bd16e1ea0',
    #   'query': str(search_en.get())
    # }

    # api_result = requests.get('http://api.weatherstack.com/current', params)

    # api_response = api_result.json()

    # try: 
    #     file = open("t.json", "w")
    #     json.dump(api_response, file, indent=2)
    #     file.close()
    # except FileNotFoundError:
    #     print ("please check for the path of the Database (JSON) file")
    #     print ("Data save failed :(")
    # except:
    #     print("an Error occured")
    # else:
    #     print ("Data saved succesfully in DB :)")

    # print('Current temperature in ', api_response['location']['name'] , 'is', api_response['current']['temperature'])

# initialize the form
main = tk.Tk()
main.title("Weather Forecast Program")
center_window(main, 500, 400)

# set upper_section or title's section
upper_section = PanedWindow(bg=third_color, height=1)
upper_section.pack(fill=BOTH, expand=0)
title = Label(upper_section, text="Weather Forecast", anchor="n", bg=third_color, fg=first_color, font=('Helvetica', 25, 'bold'))
title.pack(side='left', anchor='w', fill='both', expand=True, pady=20)

# Create a frame for the main content
main_frame = Frame(main, bg=second_color, padx=50)
main_frame.pack(side='top', fill=BOTH, expand=1)
v = tk.IntVar()
v.set(1)

title_search_frame = Frame(main_frame, bg=second_color, padx=50)
title_search_frame.pack(side='top', fill='x')

Label(title_search_frame, text="search weather details by: ", anchor="n", bg=second_color, fg=third_color, font=('Helvetica', 18, 'bold')).pack(side='left', anchor='w', fill='both', expand=True, pady=30)

radio_btn_frame = Frame(main_frame, bg=second_color, padx=50)
radio_btn_frame.pack(side='top', fill='x')

city = Radiobutton(radio_btn_frame, text="city name", bg=second_color, fg=third_color, font=('Helvetica', 14, 'bold'), variable=v, value=1, activebackground=second_color, activeforeground=third_color)
city.pack(side='left', anchor='nw')

zipcode = Radiobutton(radio_btn_frame, text="zipcode", bg=second_color, fg=third_color, font=('Helvetica', 16), variable=v, value=2, activebackground=second_color, activeforeground=third_color)
zipcode.pack(side='right', anchor='ne')

search_en_frame = Frame(main_frame, bg=second_color, padx=50)
search_en_frame.pack(side='top', fill='x')

search_en = Entry(search_en_frame, width=70, font=('Helvetica', 15), relief="flat", fg=forth_color)
search_en.pack(side='left', pady=25, anchor="w")

search_btn = HoverButton(main_frame, text="Search", relief="flat", padx=10, activebackground=third_color, activeforeground=forth_color, bg=forth_color, fg=second_color)
search_btn.pack(side='top')
# search_btn.config(command=btn_functions)

main.mainloop()