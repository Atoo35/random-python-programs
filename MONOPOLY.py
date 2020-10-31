import random
from tkinter import *
root = Tk()
class abc:
    def __init__(self,master):
        self.master=master
        self.but1=Button(text="Community Chest",command=self.nextline)
        self.but2=Button(text="Chance",command=self.nextline1)
        self.but1.pack()
        self.but2.pack()
        self.label=Label()  
        self.label.pack()

        
             
    def nextline(self):
        
        foo=['Advance to Go','Go to Jail – Go directly to jail – Do not pass Go – Do not collect $200','Bank error in your favor – Collect 200 ','Doctors fees {fee} – Pay $50','From sale of stock you get $50 ','Get Out of Jail Free {Get out of Jail, Free} – This card may be kept until needed or sold','Grand Opera Night {Opening} – Collect $50 from every player for opening night seats','Holiday {Xmas} Fund matures - Receive {Collect} $100','Income tax refund – Collect $20','It is your birthday - Collect $10 from each player','Life insurance matures – Collect $100','Pay hospital fees of $100','Pay school fees {tax} of $150','Receive $25 consultancy fee','You are assessed for street repairs – $40 per house – $115 per hotel','You have won second prize in a beauty contest – Collect $10 ','You inherit $100 ']
        abcd = random.choice(foo)
        self.message=abcd
        self.label.config(text=abcd)
        
    def nextline1(self):
        foo1=['Advance to Go','Advance to Lucknow','Advance to Ludhiana','Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times the amount thrown.','Advance token to the nearest station and pay owner twice the rental to which he/she {he} is otherwise entitled. If Station is unowned, you may buy it from the Bank.','Bank pays you dividend of $50','Get out of Jail Free – This card may be kept until needed, or traded/sold ','Go Back 3 Spaces','Go to Jail – Go directly to Jail – Do not pass Go, do not collect $200','Make general repairs on all your property – For each house pay $25 – For each hotel $100','Pay poor tax of $15','Take a trip to Kolkata','You have been elected Chairman of the Board – Pay each player $50','Your building {and} loan matures – Collect $150 ','You have won a crossword competition - Collect $100']
        abcd1 = random.choice(foo1)
        
        self.label.config(text=abcd1)
                
        
        
       
        
app=abc(root)

root.mainloop()
