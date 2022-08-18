# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 17:50:54 2022

@author: ishar
"""

from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

root=Tk()
root.geometry("800x600")
root.config(bg = '#F2CCC3')
root.title("Language Translator")

title_label=Label(root, text="Language Translator",bg='#F2CCC3',font=("Sylfaen",18,"bold","italic")) 
title_label.place(relx=0.02, rely=0.1, anchor=CENTER)

input_label=Label(root, text="Enter text", font = 'arial 13 bold', bg ='#F2CCC3')
input_label.place(relx=0.02, rely=0.2, anchor=W)

Input_text=Text(root, font = 'arial 10', height = 11, wrap = WORD, padx=5, pady=5,  bg="#FFFCF9", bd=0)
Input_text.place(relx=0.02, rely=0.5, anchor=W)
root.mainloop()

