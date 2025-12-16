import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("my apk")

my_frame=ttk.Frame()
my_frame.pack(side="left",fill="both", expand=True)

label1=tk.Label(my_frame,text="hello everyone",bg="red")
#label1.pack(side="left",fill='x',expand=True)
#label1.pack(side="left",fill='y',expand=True)
label1.pack(side="top",fill='both',expand=True)

label2=tk.Label(window,text="Good morning",bg="lightblue")
label2.pack(side="top",fill='both',expand=True)

label3=tk.Label(window,text="i am gaurav mandli",bg="lightyellow")
label3.pack(side="top",fill='both',expand=True)


window.mainloop()

