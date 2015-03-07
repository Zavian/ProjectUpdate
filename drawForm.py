# Imports
from tkinter import *
import ctypes
import main


print("Loaded drawForm.py")
# This file should contain all forms methods, like events and so on.

class Application(Frame):
    def createWidgets(self):
    	# Definition of all the components of the window
    	self.txtSearchBox = Text(height=1, width=15, name="txtSearchBox")	# The values are for cols, rows, not pixel metrics
    	self.txtSearchBox.pack({"side": "top"}, fill=X, padx=20, pady=10)
    	self.txtSearchBox.bind("<KeyRelease>", OnKeyRelease)

    	self.lstApps = Listbox(height=20, width=15, name="lstApps", selectmode=EXTENDED)
    	self.lstApps.pack({"side": "top"}, fill=X, padx=20)
    	fillList(self.lstApps) # Placeholder

    	self.btnInstall = Button(height=3, width=15, name="btnInstall", bd=2, text="Install", font=20)
    	self.btnInstall.pack({"side": "top"}, fill=X, padx=20)
    	self.btnInstall.bind("<ButtonRelease>", OnClick)

    	self.btnHelp = Button(height=2, width=5, name="btnHelp", bd=2, text="Help", font=20)
    	self.btnHelp.pack({"side": "left"}, fill=X, padx=20)
    	self.btnHelp.bind("<ButtonRelease>", OnClick)

    	self.btnAddItem = Button(height=2, width=25, name="btnAddItem", bd=2, text="Add new installer", font=20)
    	self.btnAddItem.pack({"side": "left"}, fill=X)
    	self.btnAddItem.bind("<ButtonRelease>", OnClick)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

def alert(title, text, style):
	##  Styles:
	##  0 : OK
	##  1 : OK | Cancel
	##  2 : Abort | Retry | Ignore
	##  3 : Yes | No | Cancel
	##  4 : Yes | No
	##  5 : Retry | No 
	##  6 : Cancel | Try Again | Continue
    ctypes.windll.user32.MessageBoxW(0, text, title, style)

def OnKeyRelease(event):
	# This means that the read will begin from row 0 and col 0, and it will delete the last character (which is \n)
	# http://stackoverflow.com/questions/14824163/how-to-get-the-input-from-the-tkinter-text-box-widget
	text = event.widget.get(0.0, "end-1c").lower()
	lst = app.lstApps.get(0, END)

	# Here I'll make the search
	# text : text on the search box
	# lst : items in the list
	# This section will search for items like the text, if they exist it'll select it
	if text in lst:
		for i in range(0, len(lst)):
			if lst[i].lower() == text: app.lstApps.select_set(i)
	else:
		for i in range(0, len(lst)):
			app.lstApps.select_clear(i)

	#print("Widget " + str(event.widget) + " has: " + str(text))

def OnClick(event):
	#main.test.print_me() # Placeholder to test calls from different files
	widget = str(event.widget)
	if widget == ".btnInstall": pass
	elif widget == ".btnHelp":
		alert("Help", "Welcome into the help message", 0)

def fillList(lst):
	for item in ["one", "TWO", "three", "ONE", "two", "THREE", "one", "two", "three"]:
		lst.insert(END, item)


root = Tk()
app = Application(master=root)

# Window properties
root.title('Python Updater')
root.geometry("350x525") # Width, Height (it seems these aren't not pixels)
root.resizable(width=FALSE, height=FALSE)
# END PROPERTIES



app.mainloop()
root.destroy()

