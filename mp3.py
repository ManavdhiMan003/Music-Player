import pygame
from tkinter.filedialog import askdirectory
import os
import tkinter as tk
from tkinter import *
from mutagen.id3 import ID3


root = tk.Tk()
root.minsize(500,300)


listofsongs = []
realnames = []

v = StringVar()
songlabel = Label(root,textvariable=v,width=35)

index=0 

def directorychooser():
    
    direcotry = askdirectory()
    os.chdir(direcotry)
    
    for file in os.listdir(direcotry):
        
        if file.endswith(".mp3"):
            realdir = os.path.realpath(file)
            audio = ID3(realdir)
            realnames.append(audio['TIT2'].text[0])
            
            
            listofsongs.append(file)
    
    
    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])        
    pygame.mixer.music.play()

directorychooser()

def updatelabel():
    global index
    v.set(realnames[index])
    
def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()
    
def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()
    
def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")

label = Label(root,text='Jatt da Deck')
label.pack()

listbox = Listbox(root)
listbox.pack()

realnames.reverse()
for items in realnames:
    listbox.insert(0,items)
    
realnames.reverse()    
nextbutton = Button(root,text='Next Song')
nextbutton.pack()

previoubutton = Button(root,text='Previous Song')
previoubutton.pack()

stopbutton = Button(root,text='Stop Song')
stopbutton.pack()
#root.config(bg='black')

    



nextbutton.bind("<Button-1>",nextsong)
previoubutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)

songlabel.pack()
#directorychooser()
root.mainloop()