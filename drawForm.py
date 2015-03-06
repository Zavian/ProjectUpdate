# Imports
from tkinter import *
import main

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

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()



def OnKeyRelease(event):
	# This means that the read will begin from row 0 and col 0, and it will delete the last character (which is \n)
	# http://stackoverflow.com/questions/14824163/how-to-get-the-input-from-the-tkinter-text-box-widget
	text = event.widget.get(0.0, "end-1c") 
	lst = app.lstApps.get(0, END)

	# Here I'll make the search
	# text : text on the search box
	# lst : items in the list
	# This section will search for items like the text, if they exist it'll select it
	if text in lst:
		for i in range(0, len(lst)):
			if lst[i] == text: app.lstApps.select_set(i)
	else:
		for i in range(0, len(lst)):
			app.lstApps.select_clear(i)

	#print("Widget " + str(event.widget) + " has: " + str(text))

def OnClick(event):
	main.test.print_me() # Placeholder to test calls from different files

def fillList(lst):
	for item in ["one", "two", "three", "one", "two", "three", "one", "two", "three"]:
		lst.insert(END, item)


root = Tk()
app = Application(master=root)

# Window properties
root.title('Python Updater')
root.geometry("350x525") # Width, Height (it seems these aren't not pixels)
# END PROPERTIES



app.mainloop()
root.destroy()

