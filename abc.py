from tkinter import *
main = Tk()
sec=5
def tick():
    #frame1 = Frame(main,height=640,widht=1360)
    global sec
    sec -= 1
    time['text'] = sec
    # Take advantage of the after method of the Label
    cancel_id=time.after(1000, tick)
    
    if cancel_id is not None:
        time.after_cancel(cancel_id)
        cancel_id=None
        topframe.pack_forget()
time = Label(main, fg='green')
time.pack()

    
def instructions():
    
    topframe.pack_forget()
    #topframe.pack_forget()
    #bottomframe.pack_forget()
    topframe.destroy()
    aa = Message(main,text="sefwefwfwfwgifhisuajhcwiuesfhciusdhfzcniwuskjdcniuskdjfznckwsjfngergergfasf")
    aa.pack(side=LEFT)
    Checkbutton(main, text='CheckButton').pack(side=LEFT, padx=5)
    go = Button(main,text="GO",height=3,width=20,command=tick)
    go.pack(side=LEFT)

main.title('JAM')
main.configure(bg='cyan')
topframe = Frame(main,height=1360,width=640)
topframe.pack()
bottomframe= Frame(main)
bottomframe.pack()
a = Message(topframe,font=('Comic Sans MS',50),text="JAM",bg="Cyan")
a.pack(fill=X)
welcome = Label(topframe,font=('Comic Sans MS',45),text="Welcome",bg="Cyan")
welcome.pack()
go = Button(topframe,text="GO",height=3,width=20,command=instructions)
go.pack(side=BOTTOM)

main.geometry("1360x640")
main.mainloop()
