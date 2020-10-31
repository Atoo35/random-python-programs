# run the program once and then close it and run it again and then just see all the candidate names




import os


class el(object):
    
    def __init__(self,pstname,cand1,cand2,cand3,cand4,a,b,c,d):
        self.pstname=pstname
        self.cand1=cand1
        self.cand2=cand2
        self.cand3=cand3
        self.cand4=cand4
        self.a=a #vote counting
        self.b=b   #vote counting
        self.c=c  #vote counting
        self.d=d #vote counting
        
    def getdata(self):
        pstname=input("Enter name of post:")
        self.pstname=pstname
        cand1=input("Enter name of 1st candidate:")
        self.cand1=cand1
        cand2=input("Enter name of 2nd candidate:")
        self.cand2=cand2
        ch=input("do you want to enter more(y/n)?")
        if ch=='y':
            self.cand3=input("Enter 3rd candidate:")
            #self.cand3=cand3
            ch=input("do you want to enter more?")
            if ch=='y':
                self.cand4=input("Enter 4th candidate:")
                #self.cand4=cand4
        
        
        
        f.write(pstname+"\n") #writing in file
        f.write(cand1+"\n")
        f.write(cand2+"\n")
        f.write(self.cand3+"\n")
        f.write(self.cand4+"\n")
        
    def putdata(self):
        print ("Postname:"+f3.readline())
        print ("Candidate 1:"+f3.readline())
        print ("Candidate 2:"+f3.readline())
        
        # made changes here------------------------
        candidate3 = f3.readline()			# replace self.cand3 by candidate3
        candidate4 = f3.readline()			# replace self.cand4 by candidate4
        
        if candidate3!="cand3" and candidate4!="cand4":
            print ("Candidate 3:",candidate3)
            print ("Candidate 4:",candidate4)
        elif candidate3!="cand3" and candidate4=="cand4":
            print ("Candidate 3:",candidate3)
            #f3.readline()   #skip lines if entry not written as i have initialised candidate 3 with cand3 string
        #elif self.cand3=="cand3":
           # f3.readline()  #same as above
            #f3.readline()  #same as above
        #------------------------------------------------
            
          
    def vote(self):
        """ print (self.pstname)
        print (1,self.cand1)
        print (2,self.cand2)
        if (self.cand3)!="cand3":
            print (3,self.cand3)
        if (self.cand4)!="cand4":    
            print (4,self.cand4)
        i= int(input("Enter your choice..."))
        if i==1:
            self.a+=1
        if i==2:
            self.b+=1
        if i==3:
            self.c+=1
        if i==4:
            self.d+=1"""
			#displaying candidate name from file
        print ("Postname:"+f1.readline())
        print ("Candidate 1:"+f1.readline())
        print ("Candidate 2:"+f1.readline())
        if (self.cand3)!="cand3" and self.cand4!="cand4":
            print ("Candidate 3:",f1.readline())
            print ("Candidate 4:",f1.readline())
        elif self.cand3!="cand3" and self.cand4=="cand4":
            print ("Candidate 3:",f1.readline())
            f1.readline()  
        elif self.cand3=="cand3":
            f1.readline()
            f1.readline()
            
           #getting votes
        print("\n")
        i= int(input("Enter your choice..."))
        if i==1:
            self.a+=1
        if i==2:
            self.b+=1
        if i==3:
            self.c+=1
        if i==4:
            self.d+=1
            
    def result(self):
        """print(self.pstname)
        print(1,self.cand1,self.a)
        print(2,self.cand2,self.b)
        if (self.cand3)!="cand3":
            print(3,self.cand3,self.c)
        if (self.cand4)!="cand4":
            print(4,self.cand4,self.d)"""
        print ("Postname:",f2.readline())
        print ("Candidate 1:",f2.readline(),self.a)
        print ("Candidate 2:",f2.readline(),self.b)
        if (self.cand3)!="cand3" and self.cand4!="cand4":
            print ("Candidate 3:",f2.readline(),self.c)
            print ("Candidate 4:",f2.readline(),self.d)
        elif self.cand3!="cand3" and self.cand4=="cand4":
            print ("Candidate 3:",f2.readline(),self.c)
            f2.readline()    
        elif self.cand3=="cand3":
            f2.readline()
            f2.readline() 
            
            
        print("\n")
        
        
aa=int(input("Enter Max number of posts:"))
s = [ el("pstname","cand1","cand2","cand3","cand4",0,0,0,0) for i in range(aa)]
ans='y'
ch=0
while ch!=5:
    os.system('cls')        
    print("        Elections")
    print("1) Create new")
    print("2) Display")
    print("3) Start voting")
    print("4) Result")
    print("5) Exit")
    ch=int(input("Enter choice:"))
    if ch==1:
        f=open("names.txt","w")
        for i in range(aa):
            s[i].getdata()
        f.close()
    if ch==2:
        f3=open("names.txt","r")
        
        for i in range(aa):
            s[i].putdata()
            print(input("Press ENTER to continue...."))
        f3.close()        
    if ch==3:
        while ans=='y' or ans=='Y':
            f1=open("names.txt","r") 
            for i in range(aa):
                s[i].vote()
            ans=input("Do you want to continue?")    
            f1.close()
    if ch==4:
        f2=open("names.txt","r")
        for i in range(aa):
            s[i].result()
            print(input("Press ENTER to continue...."))
        f2.close()  
    
        
#a=sys.getsizeof(s[0])
#f=open("names.txt","w")
   
#f1 = open("names.txt", "r")
#for i in range(2):
 #   print(f1.read(a))

  
























        
        
          
