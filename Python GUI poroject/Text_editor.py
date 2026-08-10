import tkinter as tk
from tkinter import filedialog


window=tk.Tk()
window.title("Text Editor")
window.rowconfigure(0,weight=1,minsize=800)
window.columnconfigure(1,weight=1,minsize=800)

def file_open(event):
    open_file=filedialog.askopenfilename(title=None)
    with open (open_file, "r") as f:
        file_read=f.read()
        Text_edit.insert("1.0",file_read)

    

def file_save(event):
    save_file=filedialog.asksaveasfilename(title=None)
    file_edit=Text_edit.get("1.0", tk.END)
    with open (save_file, "w") as f:
        f.write(file_edit)





Frame_1=tk.Frame(master=window, width=10, height=5)
Bttn_open=tk.Button(master=Frame_1, width=10, height=2,text="Open", relief="raised")
Bttn_open.bind("<Button-1>", file_open)
Bttn_save=tk.Button(master=Frame_1, width=10, height=2,text="Save", relief="raised")
Bttn_save.bind("<Button-1>",file_save)
Text_edit=tk.Text(master=window, width=100,height=30,padx=3,pady=5)



Frame_1.grid(column=0,row=0,padx=20,pady=20,sticky="n")
Text_edit.grid(column=1,row=0,sticky="nswe")
Bttn_open.grid(column=0,row=0,padx=10,pady=10,sticky="n")
Bttn_save.grid(column=0,row=2)



window.mainloop()

