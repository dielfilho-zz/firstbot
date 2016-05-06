from tkinter import *
from capture_move import CaptureMove

class BotFrame(object):

    def __init__(self):

        self.mainFrame = Tk()
        self.capture = CaptureMove()

        self.buttonUp = Button(self.mainFrame, text="^", fg="green", command=self.up_move)
        self.buttonUp.grid(row=1, column=1)

        self.buttonDown = Button(self.mainFrame, text="v", fg="green", command=self.down_move)
        self.buttonDown.grid(row=3, column=1)

        self.buttonRight = Button(self.mainFrame, text=">", fg="green", command=self.right_move)
        self.buttonRight.grid(row=2, column=2)

        self.buttonLeft = Button(self.mainFrame, text="<", fg="green", command=self.left_move)
        self.buttonLeft.grid(row=2, column=0)

        self.topFrame = Frame(self.mainFrame)

        self.buttonStartMove = Button(self.topFrame, text="START MOVE", fg="red", command=self.start_move)
        self.buttonStartMove.pack()

        self.nameLabel = Label(self.topFrame, text="PyBot")
        self.nameLabel.pack()

        self.topFrame.grid(row=0, column=3)

    def ignore(self):
        pass

    def up_move(self):
        self.capture.capture_key(self.capture.UP_KEY)

    def down_move(self):
        self.capture.capture_key(self.capture.DOWN_KEY)

    def left_move(self):
        self.capture.capture_key(self.capture.LEFT_KEY)

    def right_move(self):
        self.capture.capture_key(self.capture.RIGHT_KEY)

    def start_move(self):
        self.capture.start_moves()

    def show(self):
        self.mainFrame.mainloop()

