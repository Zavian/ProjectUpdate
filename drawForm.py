from tkinter import *

class Application(Frame):
    def createWidgets(self):
    	# Definition of all the components of the window
    	self.search_box = Text(height=1, width=15)	# The values are for cols, rows, not pixel metrics
    	self.search_box.pack({"side": "top"}, fill=X)
    	
        #self.QUIT = Button(self)
        #self.QUIT["text"] = "QUIT"
        #self.QUIT["fg"]   = "red"
        #self.QUIT["command"] =  self.quit

        #self.QUIT.pack({"side": "left"})

        #self.hi_there = Button(self)
        #self.hi_there["text"] = "Hello",
        #self.hi_there["command"] = self.say_hi

        #self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)

# Window properties
root.title('Python Updater')
root.geometry("350x525") # Width, Height (it seems these aren't not pixels)
# END PROPERTIES

app.mainloop()
root.destroy()