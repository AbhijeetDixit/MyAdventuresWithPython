from Tkinter import Tk, BOTH
from ttk import Frame, Button, Style

class GUI(Frame):
	def __init__(self, parent):
		Frame.__init__(self,parent)
		self.parent = parent
		self.initUI()
		pass

	def initUI(self):
		self.parent.title("Sample Button")
		self.style = Style()
		self.style.theme_use("default")

		self.pack(fill=BOTH, expand=1)

		quitButton = Button(self, text="Quit", command=self.quit)
		quitButton.place(x=50, y=50)


def main():

	root=Tk()
	root.geometry("250x150+300+300")
	app=GUI(root)
	app.mainloop()
	pass

if __name__ == '__main__':
	main()