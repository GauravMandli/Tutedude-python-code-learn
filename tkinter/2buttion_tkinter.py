import tkinter as tk
import tkinter.font as tfont

#tk

window = tk.Tk()
window.title("my apk")
window.minsize(width=400,height=300)


#-----
custom_font=tfont.Font(family="Times New Roman",size=19,slant='italic')#weight='bold' lakhi skay slant ni jgyaye
btn_font=tfont.Font(family="courier",size=19,weight='bold')#weight='bold lakhi skay slant ni jgyaye
label = tk.Label(text="Hello world!",font=custom_font)

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
    #print("thankyou ")this is print in console
    global counter
    counter +=1
    label.config(text=f"the button clicked {counter} times",font=btn_font)


#button
button = tk.Button(text="click",command=fun_btn)
button.pack()



window.mainloop()