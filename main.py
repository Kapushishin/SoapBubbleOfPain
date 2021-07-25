from tkinter import *
import random
root=Tk()
h, w = 400, 600
MyCanvas = Canvas(root, height=h, width=w)
MyCanvas.pack()

class App():
    def __init__(self):
        root.title('Soap Bubble Of Pain')
        SoapBubble()

class SoapBubble():
    def __init__(self):
        RandW = random.randrange(21, w-21)
        RandH = random.randrange(21, h-21)
        self.bubble = MyCanvas.create_oval(RandW - 20, RandH - 20, RandW + 20,
                                                RandH + 20, fill='blue', activefill='green')
        self.step = [random.randrange(-1, 2, 2), random.randrange(-1, 2, 2)]
        self.speed = 10
        self.MoveBubble()
        root.after(1000, SoapBubble)

    def MoveBubble(self):
        coords = MyCanvas.coords(self.bubble)
        if 600 - 20 <= coords[0] or coords[0] <= 0:
            self.step[0] *= -1
        if 400 - 20 <= coords[1] or coords[1] <= 0:
            self.step[1] *= -1
        MyCanvas.move(self.bubble, self.step[0], self.step[1])
        root.after(self.speed, self.MoveBubble)

App()
root.mainloop()