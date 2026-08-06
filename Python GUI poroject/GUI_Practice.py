import tkinter as tk
window=tk.Tk()
#label_display=tk.Label(text= 1, master=window)

def increase():
    text=int(label_display["text"])
    label_display["text"]=f"{text + 1}"
    
def decrease():
    text = int(label_display["text"])
    label_display["text"]=f"{text - 1}"    



button_increase=tk.Button(height=5, width=10, master=window, text=" + ", command=increase)
button_increase.grid(column=0, row=0, sticky="nsew")

label_display=tk.Label(height=5,width=10,master=window,text= "0")
label_display.grid(column=1, row=0, sticky="nw")


button_decrease=tk.Button(height=5, width=10, master=window, text=" - ", command=decrease)
button_decrease.grid(column=2, row=0, sticky="ne")



window.mainloop()