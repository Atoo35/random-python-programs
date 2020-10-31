from tkinter import *

class Application(Frame):
    #GUI Application

    def __init__(self, master):
        #Initialize the Frame
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        #Create new game etc...

        #Title
        self.title = Label(self,text = "Gnome")
        self.title.grid()

        #New Game
        self.new_game = Button(self,text = "New Game")
        self.new_game ["command"] = self.create_new_game
        self.new_game.grid()

        #Load Game
        self.load_game = Button(self,text = "Load Game")
        self.load_game ["command"] = self.display_saves
        self.load_game.grid()

        #Settings
        self.settings = Button(self,text = "Settings")
        self.settings ["command"] = self.display_settings
        self.settings.grid()

        #Story
        self.story = Button(self,text = "Story")
        self.story ["command"] = self.display_story
        self.story.grid()

        #Credits
        self.credits = Button(self,text = "Credits")
        self.credits ["command"] = self.display_credits
        self.credits.grid()

    def hide_widgets(self):
        #clear window
        new_game.grid_forget()

    def create_new_game(self):
        #Create new game file
        self.hide_widgets
        self.instruction = Label(self, text = "Name World:")
        self.instruction.grid()

        self.world_name = Entry(self)
        self.world_name.grid()

    def display_saves(self):
        #display saved games and allow to run
        print("saves")

    def display_settings(self):
        #display settings and allow to alter
        print("settings")

    def display_story(self):
        #display story
        print("story")

    def display_credits(self):
        #display credits
        print("credits")

root = Tk()
root.title("Welcome")
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (width,height))
app = Application(root)

root.mainloop()
