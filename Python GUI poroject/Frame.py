import tkinter as tk



window=tk.Tk()
window.rowconfigure(0,weight=2 ,minsize=5)
window.columnconfigure([0,1],weight=6,minsize=5)

frame1=tk.Frame(master=window, width=500, height=500, bg="red")
frame2=tk.Frame(master=window, width=500, height=500, bg="blue")
label_1=tk.Label(master=window,text="Hello")


frame1.grid(column=0,row=0, padx=5,pady=5)
frame2.grid(column=1,row=0, padx=5,pady=5)
label_1.grid(column=0,row=0,sticky="N")
window.mainloop()