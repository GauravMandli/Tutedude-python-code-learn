# step 1 : importing
import tkinter as tk
import tkinter.font as tfont
from tkinter import Entry # if not write so entri pahely tk.Entry karvu
from tkinter import ttk # new themd version 


# step 2 : gui interaction 

window = tk.Tk()
window.title("My Calculater")
# window.geometry("500x400")
window.minsize(width=400,height=300)

# step 3 : adding inputs

# style=ttk.Style()
# style.configure( "My.TButton",
#                 borderwidth=4,
#                 relief="solid")


#-----------------enterybox-------------------
e= ttk.Entry(window,width=30,justify="right")#  (show=*) like a password #,style= "My.TButton"
e.grid(row=0, column=0, columnspan=3, pady=10,sticky="nsew")

#-------------------button------------------
def click(num):
    result=e.get()
    e.delete(0, tk.END)
    e.insert(0,str(result) + str(num))



b1=ttk.Button(window, text="1",command=lambda:click(1))
b1.grid(row=1, column=0, padx=5, pady=5,sticky="nsew")

b2 = ttk.Button(window, text="2",command=lambda:click(2))
b2.grid(row=1, column=1, padx=5, pady=5,sticky="nsew")

b3 = ttk.Button(window, text="3",command=lambda:click(3))
b3.grid(row=1, column=2, padx=5, pady=5,sticky="nsew")
#---------------------------------------------------------------
b4 = ttk.Button(window, text="4",command=lambda:click(4))
b4.grid(row=2, column=0, padx=5, pady=5,sticky="nsew")

b5 = ttk.Button(window, text="5",command=lambda:click(5))
b5.grid(row=2, column=1, padx=5, pady=5,sticky="nsew")

b6 = ttk.Button(window, text="6",command=lambda:click(6))
b6.grid(row=2, column=2, padx=5, pady=5,sticky="nsew")
#----------------------------------------------------------------------
b7 = ttk.Button(window, text="7",command=lambda:click(7))
b7.grid(row=3, column=0, padx=5, pady=5,sticky="nsew")

b8 = ttk.Button(window, text="8",command=lambda:click(8))
b8.grid(row=3, column=1, padx=5, pady=5,sticky="nsew")

b9 = ttk.Button(window, text="9",command=lambda:click(9))
b9.grid(row=3, column=2, padx=5, pady=5,sticky="nsew")
#----------------------------------------------------------------------
b0 = ttk.Button(window, text="0",command=lambda:click(0))
b0.grid(row=4, column=0, padx=5, pady=5,sticky="nsew")


#-------------operater--------

#--------------addition------------------
def add():
    n1=e.get()
    global math
    math="addition"
    global i
    i=int(n1)
    e.delete(0, tk.END)#tk dyrect for from tkinter import END

add_b = ttk.Button(window, text="+",command=add)
add_b.grid(row=4, column=1, padx=5, pady=5,sticky="nsew")

#--------------subtraction------------------

def sub():
    n1=e.get()
    global math
    math = "subtraction"
    global i
    i=int(n1)
    e.delete(0, tk.END)


sum_b = ttk.Button(window, text="-",command=sub)
sum_b.grid(row=4, column=2, padx=5, pady=5,sticky="nsew")
#--------------------------------------------------------------

#--------------multiplection------------------

def mul():
    n1=e.get()
    global math
    math="multiplection"
    global i
    i=int(n1)
    e.delete(0, tk.END)


mul_b = ttk.Button(window, text="*",command=mul)
mul_b.grid(row=5, column=0, padx=5, pady=5,sticky="nsew")

#--------------division------------------

def div():
    n1=e.get()
    global math
    math="division"
    global i
    i=int(n1)
    e.delete(0, tk.END)
div_b = ttk.Button(window, text="/",command=div)
div_b.grid(row=5, column=1, padx=5, pady=5,sticky="nsew")


#--------------equal------------------

def equal():
    n2=e.get()
    e.delete(0,tk.END)
    
    if math == "addition":
        e.insert(0,i + int(n2))
    elif math=="subtraction":
        e.insert(0,i-int(n2))
    elif math=="multiplection":
        e.insert(0,i*int(n2))
    elif math=="division":
        e.insert(0,i/int(n2))


ans_b= ttk.Button(window, text="=",command=equal)
ans_b.grid(row=5, column=2, padx=5, pady=5,sticky="nsew")
#-------------------------------------------------------------------------

#--------------------clear-----------------

def clear():
    e.delete(0,tk.END)

clear_b = ttk.Button(window,text="clear",command=clear)
clear_b.grid(row=6, column=0,columnspan=2, padx=5, pady=10,sticky="nsew")


# step 4 : main loop

window.mainloop()