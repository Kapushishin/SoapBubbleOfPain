from tkinter import *
import tkinter as tk
import random
root=Tk()
root.geometry('600x400')
h, w = 400, 600
score = 0
mycanvas = Canvas(root, height=h, width=w)
x = random.randrange(-1, 2, 2)
y = random.randrange(-1, 2, 2)

class App():
    def __init__(self):
        root.title('Soap Bubble Of Pain')
        Menu()

class Menu():
    def __init__(self):
        self.btn = Button(text="Start", background="#555", foreground="#ccc", padx="20", pady="8", font="16")
        self.btn.bind('<Button-1>', self.click_button)
        self.btn.place(relx=.5, rely=.5, anchor="c", height=30, width=100, bordermode=OUTSIDE)

    def click_button(self, event):
        self.btn.destroy()
        mycanvas.pack()
        SoapBubble()

class Score():
    def __init__(self):
        global score
        self.lbl = Label(text="Score:"+str(score), background="#555", foreground="#ccc", padx="20", pady="8", font="16")
        self.lbl.place(relx=.5, rely=.5, anchor="c", height=30, width=100, bordermode=OUTSIDE)

class SoapBubble():
    def __init__(self):
        randw = random.randrange(21, w-21)
        randh = random.randrange(21, h-21)
        self.bubble = mycanvas.create_oval(randw - 20, randh - 20, randw + 20, randh + 20,
                                           fill='blue', activefill='green')
        self.speed = 30
        self.step = [x, y]
        self.move_bubble()
        self.speed_up()
        self.full_of_bubbles()
        root.after(3000, SoapBubble)
        mycanvas.bind('<Button-1>', self.on_click)

    def speed_up(self):
        global after_id
        if self.step[0] > 0:
            self.step[0] += 1
        else: self.step[0] -= 1
        global x
        x = self.step[0]
        if self.step[1] > 0:
            self.step[1] += 1
        else: self.step[1] -= 1
        global y
        y = self.step[1]
        after_id = root.after(5000, self.speed_up)

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
        if len(mycanvas.find_all()) > 3:
            mycanvas.delete('all')
            mycanvas.destroy()
            Score()

    def on_click(self, event):
        item = mycanvas.find_withtag(tk.CURRENT)
        global score
        current = mycanvas.find_all()
        mycanvas.delete(item)
        if current != mycanvas.find_all():
            score += 1

App()
root.mainloop()