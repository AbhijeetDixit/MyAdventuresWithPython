import sys
import Tkinter
import tkMessageBox
import tkFileDialog
from MenuFactory import *

class Editor(object):
	"""docstring for Editor"""
	def __init__(self, fileName):
		self.currentFile = fileName
		self.rootWindow = Tkinter.Tk()

	def addWidgetsNRun(self):
		# Adding a mainFrame that contains all other widgets
		mainFrame = Tkinter.Frame(self.rootWindow)
		mainFrame.pack()

		# Adding a top and bottom frame for menu and text area
		# respectively
		bottomFrame = Tkinter.Frame(self.rootWindow)
		bottomFrame.pack(side=Tkinter.BOTTOM)

		topFrame = Tkinter.Frame(self.rootWindow)
		topFrame.pack(side=Tkinter.TOP)

		# Adding a text area where all the text goes
		text = Tkinter.Text(bottomFrame,undo=True)
		text.insert(Tkinter.INSERT,"")
		text.pack()

		# Instantiating a createmenu class and creating menu
		createmenu = createMenu()
		menuBar = Tkinter.Menu(topFrame)
		filemenu = createmenu.createM(0, self.rootWindow, menuBar, text)
		editmenu = createmenu.createM(1, self.rootWindow, menuBar, text)
		formatmenu = createmenu.createM(2, self.rootWindow, menuBar, text)
		viewmenu = createmenu.createM(3, self.rootWindow, menuBar, text)
		helpmenu = createmenu.createM(4, self.rootWindow, menuBar, text)
		menuBar.add_cascade(label='File',menu=filemenu)
		menuBar.add_cascade(label='Edit',menu=editmenu)
		menuBar.add_cascade(label='Format',menu=formatmenu)
		menuBar.add_cascade(label='View',menu=viewmenu)
		menuBar.add_cascade(label='Help',menu=helpmenu)
		self.rootWindow.config(menu=menuBar)
		self.rootWindow.mainloop()



if __name__ == '__main__':
	if len(sys.argv) > 1:
		filename = sys.argv[1]
	else:
		filename = "Untitled"
	editorInstance = Editor(filename)
	editorInstance.addWidgetsNRun()