import tkinter as tk


window=tk.Tk()
window.title("Press Button")
window.columnconfigure(0,weight=1,minsize=5)
window.rowconfigure(0,weight=1,minsize=10)

def get_txt():
 
    Label_1["text"]=Entry_1.get()
    



frame_1=tk.Frame(master=window,relief="raised",borderwidth=3,height=50,width=200)
Entry_1=tk.Entry(master=frame_1, width=20)
Bttn_1=tk.Button(master=frame_1, width=10,height=0, relief="raised", text="Press", command=get_txt)
Label_1=tk.Label(master=frame_1, width=20,height=0, text=" ")



frame_1.pack()
Entry_1.grid(column=0,row=0)
Bttn_1.grid(column=0,row=1)
Label_1.grid(column=0,row=2)




window.mainloop()
