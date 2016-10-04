import Tkinter
import tkMessageBox
import tkFileDialog


def dCallback():
	tkMessageBox.showinfo('info','Button Clicked')
	pass

class createMenu(object):

	class fileMenu(object):
		"""fileMenu is the class that creates a file Menu"""

		def create(self,toplavelWindow,parentWindow,textareaWidget):
			self.toplavelWindow = toplavelWindow
			self.parentWindow = parentWindow
			self.textareaWidget = textareaWidget
			fileM = Tkinter.Menu(parentWindow,tearoff=0)
			fileM.add_command(label='New',command=self.newFileCallback)
			fileM.add_command(label='Open',command=self.openFileCallback)
			fileM.add_command(label='Save',command=self.saveFileCallback)
			fileM.add_command(label='Save As', command=self.saveAsFileCallback)
			fileM.add_separator()
			fileM.add_command(label='Exit', command=self.exitCallback)
			return fileM

		def askToSaveChanges(self):
			choice = tkMessageBox.askquestion("Warning","Do you want to save your changes?", type=tkMessageBox.YESNOCANCEL, default=tkMessageBox.YES)
			if choice == 'yes':
				file_opt = options = {}
				options['defaultextension'] = '.txt'
				options['filetypes'] = [('all files', '.*'),('text files','.txt')]
				options['initialdir'] = 'C:\\'
				options['initialfile'] = 'file.txt'
				options['parent'] = self.toplavelWindow
				options['title'] = 'Save'
				fp = tkFileDialog.asksaveasfile(mode='w', **file_opt)
				if fp is None:
					tkMessageBox.showinfo('Info', 'No file selected, not saved')
				else:
					fp.write(self.textareaWidget.get("1.0", Tkinter.END))
					fp.close()
					tkMessageBox.showinfo('Info', 'Saved')
					self.textareaWidget.delete("1.0", Tkinter.END)
				pass
			elif choice == 'no':
				self.textareaWidget.delete("1.0", Tkinter.END)
				#tkMessageBox.showinfo('Info', 'You just lost your data')
			return choice

		def exitCallback(self):
			if self.textareaWidget.edit_modified():
				self.askToSaveChanges()
			self.toplavelWindow.quit()
			pass

		def newFileCallback(self):
			if self.textareaWidget.edit_modified():
				self.askToSaveChanges()
			else:
				self.textareaWidget.delete("1.0",Tkinter.END)
			self.textareaWidget.edit_modified(False)
			self.textareaWidget.edit_reset()
			pass

		def openFileCallback(self):
			if self.textareaWidget.edit_modified():
				choice = self.askToSaveChanges()
			else:
				choice = 'no'
			if choice == 'yes' or choice == 'no':
				file_opt = options = {}
				options['defaultextension'] = '.txt'
				options['filetypes'] = [('all files', '.*'),('text files','.txt')]
				options['initialdir'] = 'C:\\'
				options['initialfile'] = ''
				options['parent'] = self.toplavelWindow
				options['title'] = 'Open'
				fp = tkFileDialog.askopenfile(mode='r', **file_opt)
				if fp is None:
					tkMessageBox.showinfo('info', 'Unable to open')
				else:
					readData = fp.read()
					self.textareaWidget.insert(Tkinter.INSERT, readData)
					self.textareaWidget.edit_modified(False)
					self.textareaWidget.edit_reset()
					fp.close()

		def saveFileCallback(self):
			if self.textareaWidget.edit_modified():
				file_opt = options = {}
				options['defaultextension'] = '.txt'
				options['filetypes'] = [('all files', '.*'),('text files','.txt')]
				options['initialdir'] = 'C:\\'
				options['initialfile'] = ''
				options['parent'] = self.toplavelWindow
				options['title'] = 'Open'
				fp = tkFileDialog.asksaveasfile(mode='w', **file_opt)
				if fp is None:
					tkMessageBox.showinfo('info', 'Cannot open the named file')
				else:
					dataToSave = self.textareaWidget.get("1.0",Tkinter.END)
					fp.write(dataToSave)
					fp.close()
					self.textareaWidget.edit_modified(False)
					self.textareaWidget.edit_reset()

		def saveAsFileCallback(self):
			if self.textareaWidget.edit_modified():
				file_opt = options = {}
				options['defaultextension'] = '.txt'
				options['filetypes'] = [('all files', '.*'),('text files','.txt')]
				options['initialdir'] = 'C:\\'
				options['initialfile'] = ''
				options['parent'] = self.toplavelWindow
				options['title'] = 'Open'
				fp = tkFileDialog.asksaveasfile(mode='w', **file_opt)
				if fp is None:
					tkMessageBox.showinfo('info', 'Cannot open the named file')	
				else:
					dataToSave = self.textareaWidget.get("1.0",Tkinter.END)
					fp.write(dataToSave)
					fp.close()
					self.textareaWidget.edit_modified(False)
					self.textareaWidget.edit_reset()

	class editMenu(object):
	
		def create(self,toplavelWindow,parentWindow,textareaWidget):
			self.toplavelWindow = toplavelWindow
			self.parentWindow = parentWindow
			self.textareaWidget = textareaWidget
			editM = Tkinter.Menu(parentWindow, tearoff=0)
			editM.add_command(label='Undo',command=self.undoCallback)
			editM.add_command(label='Redo',command=self.redoCallback)
			editM.add_separator()
			editM.add_command(label='Cut',command=dCallback)
			editM.add_command(label='Copy',command=dCallback)
			editM.add_command(label='Paste',command=dCallback)
			editM.add_command(label='Delete',command=dCallback)
			editM.add_separator()
			editM.add_command(label='Find..',command=self.findCallback)
			editM.add_command(label='Find Next', command=dCallback)
			editM.add_command(label='Replace',command=dCallback)
			editM.add_command(label='Go to..',command=dCallback)
			editM.add_separator()
			editM.add_command(label='Select All',command=dCallback)
			editM.add_command(label='Date/Time',command=dCallback)
			return editM

		def undoCallback(self):
			try:
				self.textareaWidget.edit_undo()
			except Exception, e:
				raise e
			pass

		def redoCallback(self):
			try:
				self.textareaWidget.edit_redo()
			except Exception, e:
				raise e
			pass

		def findCallback(self):
			print self.textareaWidget.index(Tkinter.INSERT)
			pass

	class formatMenu(object):
		
		def create(self,toplavelWindow, parentWindow, textareaWidget):
			formatM = Tkinter.Menu(parentWindow, tearoff=0)
			formatM.add_command(label='Word Wrap', command=dCallback)
			formatM.add_command(label='Font..', command=dCallback)
			return formatM
		
	class viewMenu(object):
	
		def create(self, toplavelWindow, parentWindow, textareaWidget):
			viewM = Tkinter.Menu(parentWindow, tearoff=0)
			viewM.add_command(label='Status Bar', command=dCallback)
			return viewM
		
	class helpMenu(object):
	
		def create(self,toplavelWindow, parentWindow, textareaWidget):
			helpM = Tkinter.Menu(parentWindow, tearoff=0)
			helpM.add_command(label='Show Help',command=self.showHelpCallback)
			helpM.add_separator()
			helpM.add_command(label='About this utility',command=self.aboutCallback)
			return helpM

		def showHelpCallback(self):
			tkMessageBox.showerror("Help","Currently the software is in development mode.\nNo help available.")
			pass

		def aboutCallback(self):
			tkMessageBox.showinfo("About Me","A simple notepad Utility.\nCreated using python 2.7\nBy - Abhijeet Dixit")
			pass

	def createM(self,mtype, toplavelWindow, parentWindow, textareaWidget):
		if mtype == 0:
			return self.fileMenu().create(toplavelWindow,parentWindow, textareaWidget)
		elif mtype == 1:
			return self.editMenu().create(toplavelWindow, parentWindow, textareaWidget)
		elif mtype == 2:
			return self.formatMenu().create(toplavelWindow, parentWindow, textareaWidget)
		elif mtype == 3:
			return self.viewMenu().create(toplavelWindow, parentWindow, textareaWidget)
		elif mtype == 4:
			return self.helpMenu().create(toplavelWindow, parentWindow, textareaWidget)
		pass