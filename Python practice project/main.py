# This code is generated using PyUIbuilder: https://pyuibuilder.com

import os
import tkinter as tk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

main = tk.Tk()
main.title("Main Window")
main.config(bg="#E4E2E2")
main.geometry("700x400")

label = tk.Label(master=main, text="To Do List")
label.config(bg="#E4E2E2", fg="#000")
label.place(x=293, y=94, height=40)


main.mainloop()