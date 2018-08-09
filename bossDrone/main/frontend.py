'''
Created on 08.08.2018

@author: Vincent Dost
'''

import tkinter as tk
from tkinter import *

root = tk.Tk()
root.attributes("-fullscreen", True)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

print(screen_height)
print(screen_width)

bttn1 = Button(root, text="Kamera")
bttn1.config(height=int(0.2*screen_height), width=screen_width)
bttn1.pack()
bttn2 = Button(root, text="Sensoren")
bttn2.config(height=int(0.2*screen_height), width=screen_width)
bttn2.pack()
bttn3 = Button(root, text="RFID")
bttn3.config(height=int(0.2*screen_height), width=screen_width)
bttn3.pack()
bttn4 = Button(root, text="Raspberry")
bttn4.config(height=int(0.2*screen_height), width=screen_width)
bttn4.pack()
bttn5 = Button(root, text="Akkustand")
bttn5.config(height=int(0.2*screen_height), width=screen_width)
bttn5.pack()

root.mainloop()