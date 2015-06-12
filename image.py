from Tkinter import Tk, Canvas, Frame, BOTH, NW
from PIL import Image 
from PIL import ImageTk

class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Pong")        
        self.pack(fill=BOTH, expand=1)
        
        self.img = Image.open("background.jpg")
        self.background = ImageTk.PhotoImage(self.img)

        canvas = Canvas(self, width=self.img.size[0], 
           height=self.img.size[1])
        canvas.create_image(10, 10, anchor=NW, image=self.background)
        canvas.pack(fill=BOTH, expand=1)


def main():
  
    root = Tk()
    ex = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()
