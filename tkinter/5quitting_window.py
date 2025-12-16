import tkinter as tk
import tkinter.font as tfont
from tkinter import Entry # if not write so entri pahely tk.Entry karvu
from tkinter import ttk # new themd version 

#tk

window = tk.Tk()
window.title("my apk")
window.minsize(width=400,height=300)


#-----
custom_font=tfont.Font(family="Times New Roman",size=19,slant='italic')#weight='bold' lakhi skay slant ni jgyaye
btn_font=tfont.Font(family="courier",size=19,weight='bold')#weight='bold lakhi skay slant ni jgyaye
label = ttk.Label(text="Hello world!",font=custom_font)

#------
# label = tk.Label(text="Hello world!", font=("Times New Roman",20,"bold"))

#label = tk.Label(text="Hello world!")
label.pack()
#label.pack(expand=True)# middle of window
#label.config(font=("courier New",25,"underline"))

#--------

label["text"]="have a nice day"
label.config(text="my new app")

#-------
counter=0
def fun_btn():
    input_text=User_input.get()
    label.config(text=input_text,font=btn_font)




#taking user input using entry
User_input = ttk.Entry(width=30)#  (show=*) like a password
User_input.pack()


#button
button = ttk.Button(text="click",command=fun_btn)
button.pack()


# window destory quit 
quit_button=ttk.Button(text="quit",command=window.destroy)
quit_button.pack()



window.mainloop()