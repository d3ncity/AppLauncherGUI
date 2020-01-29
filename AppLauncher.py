# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 01:35:36 2020

@author: 01uni
"""

import tkinter as t
from tkinter import filedialog, Text #filedialog helps us pick apps to launch, Text to display
import os #allows us to launch and run apps 

root = t.Tk() #root is similar to html body

apps = []

#if os.path.isfile('savedPaths.txt'):
#    with open('savedPaths.txt', 'r') as f:
#        tempapps = f.read()
#        tempapps = tempapps.split(',')
#        apps = [x for x in tempapps if x.strip()]

def addApp():
    
    for widget in frame.winfo_children():
        widget.destroy()
        
    filePath = filedialog.askopenfilename(initialdir="/", title="Select App",
    filetypes=(("Applications", "*.exe"),("All Files","*.*")))
    
    apps.append(filePath)
    
    for app in apps:
        label = t.Label(frame, text=app, bg="yellow")
        label.pack()
    
def runApps():
    for app in apps:
        os.startfile(app)

canvas = t.Canvas(root, height=600, width=700, bg="#C96567")
canvas.pack() #to attach it

frame = t.Frame(root, bg="white") #sort of like html divs
frame.place(relwidth=0.8,relheight=0.8, relx=0.1, rely=0.1) #to place the frame, specify dimensions, relx and rely to center the frame

chooseFile = t.Button(root, text="Choose App", padx=10, pady=5, fg="black", bg="#C96567", command=addApp)
chooseFile.pack()

launch = t.Button(root, text="Launch Apps", padx=10, pady=5, fg="black", bg="#C96567", command=runApps)
launch.pack()

root.mainloop() 

#for app in apps:
#    label = t.Label(frame, text=app)
#    label.pack()

with open('savedPaths.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')