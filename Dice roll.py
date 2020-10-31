import random
from tkinter import *
root = Tk()
class abc:
    def __init__(self,master):
        self.master=master
        self.but1=Button(text="Dice Roll",command=self.nextline)
        self.but1.pack()
        self.label=Label()  
        self.label.pack()

        
             
    def nextline(self):
        
        foo=['1','2','3','4','5','6'] 
        abcd = random.choice(foo)
        
        self.label.config(text=abcd)
        
    
        
        
       
        
app=abc(root)

root.mainloop()
