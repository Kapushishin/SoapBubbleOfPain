from tkinter import *
import random
h, w = 500, 600
RandW = random.randrange(0,w)
RandH = random.randrange(0,h)

class SoapBubbles():
    def __init__(self, master):
        self.root = master
        root.title('Soap Bubble Of Pain')
        self.MyCanvas = Canvas(self.root, height=h, width=w)
        self.MyCanvas.pack()
        self.position = [w / 2, h / 2]
        self.Bubble = self.MyCanvas.create_oval(RandW - 20, RandH - 20, RandW + 20,
                                                RandH + 20, fill="blue", activefill='red')
        self.MoveBubble()

    def MoveBubble(self):
        self.MyCanvas.move(self.Bubble, 1, 1)
        if self.MyCanvas.coords(self.Bubble)[2] < h - 20:
            root.after(10, self.MoveBubble)

root=Tk()
SoapBubbles(root)
root.mainloop()