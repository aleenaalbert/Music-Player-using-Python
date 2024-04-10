from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os

root = Tk()
root.title("Music Player")
root.geometry("920x670+290+85")
root.configure(bg="#0f1a2b")
root.resizable(False, False)

mixer.init()

def open_folder():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END, song)

def play_songs():
    music_name=playlist.get(ACTIVE)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text=music_name[0,-4])


#icon
Top = PhotoImage(file="top.png.png")
Label(root, image=Top, bg="#0f1a2b").pack()


#button
play_button = PhotoImage(file="playy (1).png")
Button(root, image=play_button, bg="#0f1a2b", bd=0, command=play_songs).place(x=130, y=415)

pause_button = PhotoImage(file="pauseeeeee (1).png")
Button(root, image=pause_button, bg="#0f1a2b", bd=0, command=mixer.music.pause).place(x=130, y=500)


next_button = PhotoImage(file="righttttt.png")
Button(root, image=next_button, bg="#0f1a2b", bd=0, command=mixer.music.unpause).place(x=230, y=500)

back_button = PhotoImage(file="lefttttt.png")
Button(root, image=back_button, bg="#0f1a2b", bd=0, command=mixer.music.pause).place(x=30, y=500)

#label
music= Label(root,text="", font=("arial", 15), fg="white",bg="#0f1a2b")
music.place(x=150, y=340, anchor="center")

#music
Menu = PhotoImage(file="music.png.png")
Label(root, image=Menu, bg="#0f1a2b").pack(padx=10, pady=50, side=RIGHT)

music_frame = Frame(root, bd=2, relief=RIDGE)
music_frame.place(x=330, y=350, width=560, height=250)

Button(root, text="Open Folder", width=15, height=2, font=("arial", 10, "bold"), fg="white", bg="#000000", command=open_folder).place(x=330, y=300)

scroll = Scrollbar(music_frame)
playlist = Listbox(music_frame, width=100, font=("arial", 10), bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=scroll.set)

scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT, fill=BOTH)

root.mainloop()



