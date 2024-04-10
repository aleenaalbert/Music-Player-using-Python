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

def open_folder():
    path=filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)
        print(songs)

#icon
image_icon=PhotoImage(file="logo.png.png")
root.iconphoto(False,image_icon)
                      
Top=PhotoImage(file="top.png.png")
Label(root,image=Top,bg="#0f1a2b").pack()

#logo
Logo=PhotoImage(file="logo.png.png")
Label(root,image=Logo,bg="#0f1a2b").place(x=65,y=115)

#button
play_button=PhotoImage(file="play.png.png")
Button(root,image=play_button,bg="#0f1a2b").place(x=100,y=400)

pause_button=PhotoImage(file="pause.png.png")
Button(root,image=pause_button,bg="#0f1a2b").place(x=30,y=500)

next_button=PhotoImage(file="next.png.png")
Button(root,image=next_button,bg="#0f1a2b").place(x=115,y=500)

back_button=PhotoImage(file="back.png.png")
Button(root,image=back_button,bg="#0f1a2b").place(x=200,y=500)

#music
Menu=PhotoImage(file="music.png.png")
Label(root,image=Menu,bg="#0f1a2b").pack(padx=10,pady=50,side=RIGHT)

music_frame=Frame(root,bd=2,relief=RIDGE)
music_frame.place(x=330,y=350,width=560,height=250)

Button(root,text="Open Folder",width=15,height=2,font=("arial",10,"bold"),fg="white",bg="#21b3e",command=open_folder).place(x=330,y=300)

scroll = Scrollbar(music_frame)
playlist=Listbox(music_frame,width=100,font=("arial",10),bg="#333333",fg="grey",selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=scroll.set)

scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT,fill=Y)
playlist.pack(side=LEFT,fill=BOTH)



