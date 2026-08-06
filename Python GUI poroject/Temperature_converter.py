#This program will conver the degree to farhenheit

import tkinter as tk


def far_to_cel():
    entry_value=float(entry_tem.get())
    cel=float((entry_value -32)*(5/9))
    label_2["text"]=f"{cel:.2f} °C "
   
   

window=tk.Tk()
window.title("Temprature converter")
window.resizable(width=True,height=True)


frame_1=tk.Frame(master=window,relief="raised",borderwidth=3,height=50,width=200)
entry_tem=tk.Entry(master=frame_1, width=10, relief="sunken" ,borderwidth= 1)
click_button=tk.Button(master=frame_1,width=2, text=" » " , command=far_to_cel, background="white", relief="raised")
label_1=tk.Label(master=frame_1, text=" °F ")
label_2=tk.Label(master=frame_1, text=" °C ")

frame_1.pack()
entry_tem.grid(column=0,row=0)
click_button.grid(column=2, row=0)
label_1.grid(column=1, row=0)
label_2.grid(column=3,row=0)






window.mainloop()

