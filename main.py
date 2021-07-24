from tkinter import *
import random
root=Tk()
h, w = 400, 600
MyCanvas = Canvas(root, height=h, width=w)
MyCanvas.pack()

class App():
    def __init__(self):
        root.title('Soap Bubble Of Pain')
        #for i in range(10):
        a = SoapBubble()
        b = SoapBubble()

class SoapBubble():
    def __init__(self):
        RandW = random.randrange(0, w)
        RandH = random.randrange(0, h)
        self.bubble = MyCanvas.create_oval(RandW - 20, RandH - 20, RandW + 20,
                                                RandH + 20, fill='blue', activefill='red')
        self.mooving = [3, 3]
        self.MoveBubble()

    def MoveBubble(self):
        coords = MyCanvas.coords(self.bubble)
        if 600 - 40 <= coords[0] or coords[0] <= 0:
            self.mooving[0] *= -1
        if 400 - 40 <= coords[1] or coords[1] <= 0:
            self.mooving[1] *= -1
        MyCanvas.move(self.bubble, self.mooving[0], self.mooving[1])
        root.after(20, self.MoveBubble)

App()
root.mainloop()