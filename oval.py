#get tkinter ready

from tkinter import *
import time
window = Tk()
canvas = Canvas(window,width=800, height=600, bg='white')
canvas.pack()

#Create eggs of different colours

egg1=canvas.create_oval(4,45,35,95,fill='green',outline='black')

x1,y1,x2,y2=canvas.coords(egg1)

egg2=canvas.create_oval(x1+70,y1+70,x2+70,y2+70,fill='red',outline='black')

egg3=canvas.create_oval(x1+150,y1+150,x2+150,y2+150,fill='yellow',outline='black')

egg4=canvas.create_oval( x1+500,y1+500,x2+500,y2+500,fill='red',outline='black')             

egg5=canvas.create_oval(x1+300,y1+300,x2+300,y2+300,fill='yellow',outline='black')

egg6=canvas.create_oval(x1+230,y1+230,x2+230,y2+230,fill='green',outline='black')

egg7= canvas.create_oval(x1+200,y1+200,x2+200,y2+200,fill='blue',outline='black')

egg8= canvas.create_oval(x1+430,y1+430,x2+430,y2+430,fill='blue',outline='black')
window.mainloop()

                              
