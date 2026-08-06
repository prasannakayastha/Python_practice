import tkinter as tk

window=tk.Tk()
window.title("Address Entry Form")


Frame_First_Name=tk.Frame(master=window,relief="raised",borderwidth=5)

Frame_Buttons=tk.Frame(master=window, relief="raised",borderwidth=5)
Buttons_clear=tk.Button(master=Frame_Buttons, height=1,width=10,text="Clear")
Buttons_submit=tk.Button(master=Frame_Buttons, height=1,width=10,text="Submit")

Label_First_Name=tk.Label(master=Frame_First_Name, text="First Name")
Label_Last_Name=tk.Label(master=Frame_First_Name, text="Last Name")
Label_Address_1=tk.Label(master=Frame_First_Name, text="Address 1")
Label_Country=tk.Label(master=Frame_First_Name, text="Country")

Entry_First_Name=tk.Entry(master=Frame_First_Name, width=40)
Entry_Last_Name=tk.Entry(master=Frame_First_Name, width=40)
Entry_Address_1=tk.Entry(master=Frame_First_Name, width=40)
Entry_Country=tk.Entry(master=Frame_First_Name, width=40)

Frame_First_Name.grid(column=0, row=0)
Frame_Buttons.grid(column=0,row=1)

Label_First_Name.grid(column=0,row=0)
Label_Last_Name.grid(column=0,row=1)
Label_Address_1.grid(column=0,row=2)
Label_Country.grid(column=0,row=3)

Entry_First_Name.grid(column=1,row=0)
Entry_Last_Name.grid(column=1,row=1)
Entry_Address_1.grid(column=1,row=2)
Entry_Country.grid(column=1,row=3)

Buttons_clear.grid(column=0,row=0)
Buttons_submit.grid(column=1,row=0)




window.mainloop()


