from tkinter import *
def bye():
    print("bye")
root = Tk()
root.title('Timer')
#root.state('zoomed')

def countdown(count):
    # change text in label        
    time['text'] = count

    if count > 0:
        # call countdown again after 1000ms (1s)
        root.after(1000, countdown, count-1)
    
   
        

time = Label(root, fg='green')
time.pack()
Button(root, fg='blue', text='Start', command=countdown(5)).pack()


root.mainloop()
