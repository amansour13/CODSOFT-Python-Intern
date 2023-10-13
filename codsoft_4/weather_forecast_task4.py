"""
Task 4       : weather forecast App
Author       : Ahmed Mansour
Version      : v0.1
Release Date : 14/10/2023

Description:
This weather forecast App is a simple program that show the weather details of a specific city based on user input
which is the city or its zipcode.

Contact Information:
If you have any questions, suggestions, or feedback, feel free to reach out to the author:
- Email: a.mansour1345@gmail.com
"""

from tkinter import *

import tkinter as tk
from tkinter import ttk
import requests
first_color, second_color, third_color, forth_color = "#DAFFFB", "#64CCC5", "#176B87", "#04364A"


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

def request (query):
    params = {
      'access_key': 'a718126fecd2f38fe9a9411bd16e1ea0',
      'query': query
    }

    api_result = requests.get('http://api.weatherstack.com/current', params)

    api_response = api_result.json()

    if ('success' in api_response):
        return False
    else:
        return (
            api_response['location']['name'],
            api_response['location']['country'],
            api_response['current']['observation_time'],
            api_response['current']['temperature'],
            api_response['current']['weather_descriptions'],
            api_response['current']['humidity'],
        )

def weather_details_screen(screen, data):
    name_frame = Frame(screen, bg=second_color, padx=50)
    name_frame.pack(side='top', fill='x')
    Label(name_frame, text=data[0], anchor="n", bg=third_color, fg=first_color, font=('Helvetica', 12, 'bold'), pady=5).pack(side='left', anchor='w', fill='both', expand=True)
    country_frame = Frame(screen, bg=second_color, padx=50)
    country_frame.pack(side='top', fill='x')
    Label(country_frame, text=data[1], anchor="n", bg=third_color, fg=first_color, font=('Helvetica', 10)).pack(side='left', anchor='w', fill='both', expand=True)

    rest_data_frame = Frame(screen, bg=second_color, padx=50)
    rest_data_frame.pack(side='top', fill='x')
    Label(rest_data_frame, text=str(data[3])+'°C', anchor="n", bg=second_color, fg=forth_color, font=('Helvetica', 70)).pack(side='right', anchor='e', pady=50)
    left_hand_data_frame =   Frame(rest_data_frame, bg=second_color)
    left_hand_data_frame.pack(side='left', anchor='w')
    Label(left_hand_data_frame, text="humidity: " + str(data[5]) + ' g/kg', anchor="w", bg=second_color, fg=forth_color, font=('Helvetica', 11)).pack(side='top', anchor='w')
    Label(left_hand_data_frame, text="Time: " + data[2], anchor="w", bg=second_color, fg=forth_color, font=('Helvetica', 11)).pack(side='top', anchor='w')
    
    desc = ""
    for i in data[4]:
            desc += i + '\n'

    Label(left_hand_data_frame, text= desc, wraplength= 200, anchor="w", bg=second_color, fg=forth_color, font=('Helvetica', 11)).pack(side='top', anchor='w')

    back_btn = HoverButton(screen, text="< back", relief="flat", padx=10, activebackground=third_color, activeforeground=forth_color, bg=forth_color, fg=second_color, font=('Helvetica', 14))
    back_btn.pack(side='top')
    back_btn.config(command= lambda: (screen.destroy(), main.deiconify()))


        
def error_screen(screen):
    main_frame = Frame(screen, bg=second_color, pady=100)
    main_frame.pack(fill=BOTH, expand=1)

    err_lbl = Label(main_frame, wraplength=400, text="Error (cannot find your city):\nplease double check your search entry", bg=second_color, fg=third_color, font=('Helvetica', 20, 'bold'))
    err_lbl.pack(side='top')

    back_btn = HoverButton(main_frame, text="< back", relief="flat", padx=10, activebackground=third_color, activeforeground=forth_color, bg=forth_color, fg=second_color, font=('Helvetica', 14))
    back_btn.pack(side='top', pady=20)
    back_btn.config(command= lambda: (screen.destroy(), main.deiconify()))

def search():
    #initialize a new window for the query
    details_screen = tk.Tk()
    details_screen.config(bg=second_color)
    center_window(details_screen, 500, 400)
    # hiding the main screen
    main.withdraw()
    details_screen.protocol("WM_DELETE_WINDOW", lambda: (details_screen.destroy(), main.destroy()))
    
    # send request and check if it gets data or not
    if (bool(request(search_en.get()))):
        # success screen
        details_screen.title(search_en.get())
        weather_details_screen(details_screen, request(search_en.get()))
    else:
        # error screen if the entered search is incorrect
        details_screen.title('Error')
        error_screen(details_screen)
    
    details_screen.mainloop()


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

Label(title_search_frame, text="search your city by: ", anchor="n", bg=second_color, fg=third_color, font=('Helvetica', 18, 'bold')).pack(side='left', anchor='w', fill='both', expand=True, pady=30)

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
search_btn.config(command=search)

main.mainloop()