from tkinter import *
root =Tk()
class mainwindow:
    def __init__(self,master):
        self.master=master
        self.frame=Frame(self.master,height=300,width=400)
        self.frame1=Frame(self.master,height=200,width=200)
        self.frame.pack()
        self.frame1.pack()
        self.go=Button(self.frame,text="Home",width=31).pack(side=LEFT)
        self.go=Button(self.frame,text="Gallery",width=31).pack(side=LEFT)
        self.go=Button(self.frame,text="About us",width=31).pack(side=LEFT)
        self.go=Button(self.frame,text="Events",width=31).pack(side=LEFT)
        self.go=Button(self.frame,text="COntact us",width=31).pack(side=LEFT)
        self.go=Button(self.frame,text="Extra page",width=31).pack(side=LEFT)
        self.welcome=Label(self.frame1,font=('Comic Sans MS',30),text="Welcome").grid(row=0)        
































root.configure(bg="cyan")
root.title('place')
root.geometry("200x100")
app=mainwindow(root)
root.mainloop()        
