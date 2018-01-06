from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

class FileEditor:
    def __init__(self):
        window = Tk()
        window.title("Simple Text Editor")

        menubar = Menu(window)
        window.config(menu = menubar)

        operationMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=operationMenu)
        operationMenu.add_command(label="Open", command=self.openFile)
        operationMenu.add_command(label="Save", command=self.saveFile)

        frame = Frame(window)
        frame.grid(row = 1, column=1)

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.text = Text(frame, width=40, height=20, wrap=WORD,
                         yscrollcommand = scrollbar.set)
        self.text.pack()
        scrollbar.config(command=self.text.yview)

        window.mainloop()

    def openFile(self):
        filenameForReading = askopenfilename()
        infile = open(filenameForReading, "r")
        self.text.insert(END, infile.read())
        infile.close()

    def saveFile(self):
        filenameForWriting = asksaveasfilename()
        outfile = open(filenameForWriting, "w")
        outfile.write(self.text.get(1.0, END))
        outfile.close()

FileEditor()