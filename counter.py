"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 0123456
Name:       Xxxx Yyyyyy
Email:      xxxx.yyyyyy@tuni.fi

Code template for counter program.
"""

from tkinter import *
import sys


def quit():
    sys.exit(0)


def buildWindow():
    root = Tk()

    frame = Frame(root)
    label = Label(frame)

    increaseButton = Button(label)
    decreaseButton = Button(label)
    quitButton = Button(label)
    resetButton = Button(label)

    root.mainloop()


def main():
    buildWindow()


if __name__ == '__main__':
    main()
