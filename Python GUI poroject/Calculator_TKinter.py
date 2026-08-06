#TKinter GUI project. I would like to give a week to learn Tkinter GUI and build something.
#2-3 days of tutorial 
#2-3 days building a small project
# This is my target.
#Lets go!!!!

import tkinter as tk

window=tk.Tk()
for y in range(3):
    window.columnconfigure(y,weight=1, minsize=50)
    window.rowconfigure(y,weight=1,minsize=50)


Button_digit=tk.Button(master=window,height=2, width=5, borderwidth=1,relief=tk.RAISED, text="1")
Button_digit.grid(column=0, row=0, padx=5, pady=5)
Button_digit=tk.Button(master=window,height=2, width=5, borderwidth=1,relief=tk.RAISED, text="2")
Button_digit.grid(column=1, row=0, padx=5, pady=5)
Button_digit=tk.Button(master=window,height=2, width=5, borderwidth=1,relief=tk.RAISED, text="3")
Button_digit.grid(column=2, row=0, padx=2, pady=2)



window.mainloop()




