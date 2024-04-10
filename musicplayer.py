from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os

root=Tk()
root.title("Music Player")
root.geometry("920x670+290+85")
root.configure(bg="#0f1a2b")
root.resizable(False,False)

mixer.init()

#icon
Top=PhotoImage(file="top.png")
Label(root,image=Top,bg="0f1a2b").pack()

#button
play_button=PhotoImage(file="play.png")
Button(root,image=play_button,bg="0f1a2b",bd=0).place(x=100,y=400)



root.mainloop()

