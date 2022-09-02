# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 17:50:54 2022

@author: ishar
"""

from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root=Tk()
root.geometry("800x600")
root.config(bg = '#F2CCC3')
root.title("Language Translator")

title_label=Label(root, text="Language Translator",bg='#F2CCC3',font=("Sylfaen",18,"bold","italic")) 
title_label.place(relx=0.4, rely=0.1, anchor=CENTER)

input_label=Label(root, text="Enter text", font = 'arial 13 bold', bg ='#F2CCC3')
input_label.place(relx=0.02, rely=0.2, anchor=W)
languages= list(LANGUAGES.values())
combo= ttk.Combobox(state="readonly", values=languages, width=10)
combo.set("english")
combo.place(relx=0.3, rely=0.2, anchor=CENTER)
Input_text=Text(root, font = 'arial 10', height = 11, wrap = WORD, padx=5, pady=5,  bg="#FFFCF9", bd=0, width=40)
Input_text.place(relx=0.02, rely=0.5, anchor=W)
output_label=Label(root, text="Output", font = 'arial 13 bold', bg ='#F2CCC3')
output_label.place(relx=0.6, rely=0.2, anchor=W)
languages2= list(LANGUAGES.values())
combo2= ttk.Combobox(state="readonly", values=languages2, width=10)
combo2.set("english")
combo2.place(relx=0.8, rely=0.2, anchor=CENTER)
Output_text=Text(root, font = 'arial 10', height = 11, wrap = WORD, padx=5, pady=5,  bg="#FFFCF9", bd=0, width=40)
Output_text.place(relx=0.97, rely=0.5, anchor=E)
btn=Button(root, text="Translate",font = 'arial 10', bg="blue", fg="white", activebackground="black", relief=FLAT, pady=10, command=Translate)
btn.place(relx=0.5, rely=0.7, anchor=CENTER)

def Translate():
    obj_trans=Translator()
    try:
        translated= obj_trans.translate(Input_text.get(), 0, END, combo.get(), combo2.get())
        Input_text.delete(0, END)
        Output_text.insert(END, translated)
    except:
        print("Try again")
        
label=Label(root, text="Created by Isha", bg="#F2CCC3", font = 'arial 10 bold')
label.place(relx=0.5, rely=0.99, anchor=CENTER)
root.mainloop()

