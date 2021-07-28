from tkinter import *
import tkinter as tk
import random
root=Tk()
root.geometry('600x400')
h, w = 400, 600
mycanvas = Canvas(root, height=h, width=w)
mycanvas.pack()

class App():
    def __init__(self):
        root.title('Soap Bubble Of Pain')
        SoapBubble()

class SoapBubble():
    def __init__(self):
        randw = random.randrange(21, w-21)
        randh = random.randrange(21, h-21)
        self.t = 0
        self.bubble = mycanvas.create_oval(randw - 20, randh - 20, randw + 20, randh + 20,
                                           fill='blue', activefill='green')
        self.step = [random.randrange(-1, 2, 2), random.randrange(-1, 2, 2)]
        self.speed = 30
        self.move_bubble()
        self.speed_up()
        self.full_of_bubbles()
        root.after(3000, SoapBubble)
        mycanvas.bind('<Button-1>', self.on_click)

    def speed_up(self):
        if self.step[0] > 0:
            self.step[0] += 3
        else: self.step[0] -= 3
        if self.step[1] > 0:
            self.step[1] += 3
        else: self.step[1] -= 3
        root.after(5000, self.speed_up)

    def move_bubble(self):
        coords = mycanvas.coords(self.bubble)
        crossing = mycanvas.find_overlapping(coords[0], coords[1], coords[2], coords[3])

        for i in crossing:
            if not self.bubble == i:
                self.step[0] *= -1
                self.step[1] *= -1

        if w - 40 <= coords[0] or coords[0] <= 0:
            self.step[0] *= -1
        if h - 40 <= coords[1] or coords[1] <= 0:
            self.step[1] *= -1

        mycanvas.move(self.bubble, self.step[0], self.step[1])
        root.after(self.speed, self.move_bubble)

    def full_of_bubbles(self):
        if len(mycanvas.find_all()) > 15:
            mycanvas.destroy()

#        self.t += 1
#        if self.t >= 300:
#            mycanvas.delete(mycanvas.find_all()[0])

    def on_click(self, event):
        item = mycanvas.find_withtag(tk.CURRENT)
        mycanvas.delete(item)

App()
root.mainloop()