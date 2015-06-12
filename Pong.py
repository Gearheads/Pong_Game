import sys
import random
import pygame
from PIL import Image, ImageTk
from Tkinter import Tk, Frame, Canvas, ALL, BOTH, NW

WIDTH=1000
HEIGHT=500

def initGame(self):
    self.up=False
    self.down=False
    self.w=False
    self.s=False
    self.inGame=False

def onKeyPressed(self, e):
    key = e.keysym
    if key == "Up" and not self.down:
        self.up = True

    if key == "Down" and not self.up:
        self.down = True

    if key =="W" and not self.s:
        self.w = True
        self.s = False

#Creates the paddle objects
class Paddle:
    def __init__(self,image,width,height,speed):
        self.speed=speed
        self.image=image
        self.witdh=width
        self.height=height
    
#Creates the board
class Pong(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent=parent
        self.initUI()

    def initUI(self):
        self.parent.title('Pong')
        self.pack(fill=BOTH, expand=1)

        self.img=Image.open("background.jpg")
        self.background=ImageTk.PhotoImage(self.img)

        canvas=Canvas(self,width=self.img.size[0],height=self.img.size[1])
        canvas.create_image(10,10,anchor=NW,image=self.background)
        canvas.pack(fill=BOTH, expand=1)
        
def main():
    root=Tk()
    pong=Pong(root)
    paddleImg=Image.open("paddle.jpg")
    player1=Paddle(paddleImg, 1, 5, 1)
    player2=Paddle(paddleImg, 9, 5, 1)
    root.mainloop()

if __name__=='__main__':
    main()
