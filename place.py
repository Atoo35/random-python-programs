from tkinter import *
root = Tk()

class jam:
    def __init__(self,master):
        self.master = master
        self.frame=Frame(master,height=640,width=1360)
        self.frame1=Frame(master,height=640,width=1360)
        self.frame2=Frame(master,height=640,width=1360)
        self.frame3=Frame(master,height=640,width=1360)
        self.frame.pack()
        self.label=Label(self.frame,text="JAM",font=('Comic Sans MS',60)).pack(fill=X)
        self.welcome=Label(self.frame,font=('Comic Sans MS',45),text="Welcome").pack()
        self.go=Button(self.frame,text="GO",height=3,width=20,command=self.instructions).pack(side=BOTTOM)
        
        
    def instructions(self):
        self.frame.pack_forget()
        self.frame.destroy()
        self.frame3.pack()
        self.message= Message(self.frame3,text="sefwefwfwfwgifhisuajhcwiuesfhciusdhfzcniwuskjdcniuskdjfznckwsjfngergergfasf",width=300).place(x=20,y=20)
        self.check=Checkbutton(self.frame3, text='CheckButton').place(x=350,y=20)
        self.but=Button(self.frame3,text="GO",height=3,width=20,command=self.timer).pack(side=BOTTOM)

    def timer(self):
        
        self.frame2.pack()
        self.time = Label(frame2,bg="cyan")
        self.time.place(x=200,y=200)
        self.countdown(5)
    def countdown(self,count):
        self.frame3.pack_forget()
       
        # change text in label        
        time['text'] = count

        if count > 0:
            # call countdown again after 1000ms (1s)
            self.master.after(1000, self.countdown, count-1)
            
        







root.configure(bg="cyan")
root.title('place')
root.geometry("200x100")
app=jam(root)
root.mainloop()
