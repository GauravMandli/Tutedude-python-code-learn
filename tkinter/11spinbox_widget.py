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


label = ttk.Label(text="Hello world!",font=custom_font,padding=15)
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
quit_button.pack(pady=10)#button pading is diffrent 

#seprter
sep=ttk.Separator(orient="horizontal")
sep.pack(fill='x')


text = tk.Text(height=5,width=25)
text.pack(pady=10)#text ma pan aem j 
text.focus()#for curser

text.insert("1.0","Enter your comments:- ")#1 is line number and 0 is charcter number

def text_function():
    text_data=text_data=text.get("1.0","end")
    print(text_data)

text_button=ttk.Button(text="get text",command=text_function)
text_button.pack()

#----------------disable enable for-------

# text["state"]="disabled"

# def enable_text():
#     text["state"]="normal"

# enable_button=ttk.Button(text="enable text box",command=enable_text)
# enable_button.pack()

#-----------------end-----------------


#------checkbutton---------------

#check_option=tk.IntVar()
check_option=tk.StringVar()
#check_option=tk.BooleanVar()

def check_option_task():
    print(check_option.get(),type(check_option.get()))

check_button=ttk.Checkbutton(text="Agree with terms & condition ?",variable=check_option,
                             command=check_option_task,onvalue="yes",offvalue="No")
check_button.pack()

#-------------end---------------------


#------radio button--------------------------
radio_value=tk.StringVar()

def get_radio_value():
    print(radio_value.get())

option_1=ttk.Radiobutton(text="Male",variable=radio_value,value="male",command=get_radio_value)
option_2=ttk.Radiobutton(text="Female",variable=radio_value,value="female",command=get_radio_value)
option_1.pack()
option_2.pack()

#-------end----------------------------

#------------combobox-----------------

selected_country=tk.StringVar()

countries=ttk.Combobox(textvariable=selected_country,value=("australia","canada","india","shreelanka"))
countries["state"]="readonly"
countries.pack()

def display_country(event):
    msg=f"selected country is {selected_country.get()}"
    #country_label = ttk.Label(text=selected_country.get())
    country_label = ttk.Label(text=msg)#ahi msg vadu che and upar dyrct che
   
    country_label.pack()
    print(f"selected country is {selected_country.get()}")
    
countries.bind("<<ComboboxSelected>>",display_country)
#------------end-----------------


#------------listbox-----------------

food_item=("panjabi","chiniz","pulav","paubhaji","dosa")
fav_food=tk.StringVar(value=food_item)

food_list=tk.Listbox(listvariable=fav_food,height=5,selectmode="ectended")
food_list.pack()

def get_fav_food(event):
    food_indices = food_list.curselection()
    for i in food_indices:
        print(food_list.get(i))


food_list.bind("<<ListboxSelect>>",get_fav_food)
#------------end-----------------

#------------Spinbox-----------------
counter=tk.IntVar(value=10)

def get_spin_box_value():
    print(f"current spin box value {spin_box.get()}")

# spin_box=ttk.Spinbox(from_=0,to=20, textvariable=counter,wrap=True,command=get_spin_box_value)
#spin_box=ttk.Spinbox(values=(10,20,30,40,50), textvariable=counter,wrap=True,command=get_spin_box_value)
spin_box=ttk.Spinbox(values=tuple(range(5,105,5)), textvariable=counter,wrap=True,command=get_spin_box_value)

spin_box.pack()

print(f"initial value {spin_box.get()}")
#------------end-----------------
window.mainloop()