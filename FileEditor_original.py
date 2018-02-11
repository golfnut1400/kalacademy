from tkinter import *
# open a file
from tkinter.filedialog import askopenfilename
# save a file
from tkinter.filedialog import asksaveasfilename


class FileEditor:
    #constructor
    def __init__(self):
        #create a window
        window = Tk()
        # set title of window
        window.title("Simple Text Editor")

        #creating a menu
        menubar = Menu(window)
        #
        window.config(menu = menubar)

        # this iwll be on the menubar,
        # tearoff= 0
        operationMenu = Menu(menubar, tearoff=0)
        # .add_cascacade will open another menu
        menubar.add_cascade(label="File", menu=operationMenu)

        # when user click Open will open a file
        operationMenu.add_command(label="Open", command=self.openFile)
        # when selected will save file
        operationMenu.add_command(label="Save", command=self.saveFile)

        #frame
        frame = Frame(window)
        # this is just 1 frame and inside a grid
        frame.grid(row = 1, column=1)

        # scrollbar inside a frame
        scrollbar = Scrollbar(frame)
        # create a scrollbar ... all upper case
        scrollbar.pack(side=RIGHT, fill=Y)

        # this is where the text will be created and put into self.text
        self.text = Text(frame, width=40, height=20, wrap=WORD,
                         yscrollcommand = scrollbar.set)  # when you scroll on the textbox the scrollbar will move


        # text get place
        self.text.pack()
        # change scrollbar
        scrollbar.config(command=self.text.yview)

        window.mainloop()

    def openFile(self):
        filenameForReading = askopenfilename()
        infile = open(filenameForReading, "r")  #"r" = readmode
        self.text.insert(END, infile.read())   # END will put file to end ...read from a file
        infile.close()

    def saveFile(self):
        # writing to a file
        filenameForWriting = asksaveasfilename()
        # first open the file for writing mode
        outfile = open(filenameForWriting, "w") # 'w' write mode

        outfile.write(self.text.get(1.0, END))  # .get to read everything
        outfile.close()

FileEditor()
