from Tkinter import Tk, Frame, BOTH

class GUI(Frame):
	def __init__(self, parent):
		Frame.__init__(self,parent,background="white")
		self.parent = parent
		self.initUI()
		pass

	def initUI(self):
		self.parent.title("Example")
		self.pack(fill=BOTH, expand=1)


def main():

	root=Tk()
	root.geometry("250x150+300+300")
	app=GUI(root)
	app.mainloop()
	pass

if __name__ == '__main__':
	main()