__author__ = 'Ciaran'
#Lab test 23/04/15
#Program to open files in window using tkinker
#OPened files available are source code plain text and html, also any other type of file

#omport the interface modules
from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox
import os,time

#Gui class to create all parts of the gooey
class GUI():
    def __init__(self, parent):
        self.parent = parent
        self.parent.protocol("WM_DELETE_WINDOW", self.catch_destroy)
        #close application code

        self.parent.option_add("*tearOff", FALSE)#Stops user using tear off command

        #Menu button with sub commands open and exit
        self.menu = Menu(self.parent)
        self.file_menu = Menu(self.menu)
        self.file_menu.add_command(label="Open", command=self.open_file)#open command
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.catch_destroy)#close command

        self.help_menu = Menu(self.menu)
        self.help_menu.add_command(label="About", command=self.about)#About label to display about information

        self.menu.add_cascade(label="File", menu=self.file_menu)#Makes the menu a drop done format
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.parent.config(menu=self.menu)

        self.frame1 = ttk.Frame(self.parent, padding=10, border=2)
        self.frame1.grid(row=0, column=0)

        #Displays Python lab test above the text window
        self.file_chosen= StringVar()
        self.file_chosen.set("Filename here")
        self.filelabel = Label(self.frame1, textvariable=self.file_chosen)
        self.filelabel.grid(row=0, column=0)

        self.filesize = StringVar()
        self.createdate = StringVar()

        #diplays only one row of text and no divide horizontaly
        self.text1 = Text(self.frame1, width=100, wrap=NONE)
        self.text1.grid(row=1, column=0)

        #inserts vertical scrollbar
        self.yscroll = ttk.Scrollbar(self.frame1, orient=VERTICAL, command=self.text1.yview)
        self.yscroll.grid(row=1, column=1, sticky=N+S)
        #Inserts horizontal scrollbar
        self.xscroll = ttk.Scrollbar(self.frame1, orient=HORIZONTAL, command=self.text1.xview)
        self.xscroll.grid(row=2, column=0, sticky=W+E)

        self.text1["yscrollcommand"] = self.yscroll.set
        self.text1["xscrollcommand"] = self.xscroll.set

    def catch_destroy(self):#function for if the user attempts to exit the programe a warning message pops up asking if they are sure they want to do this
        if messagebox.askokcancel("Quit", "Are you sure?"):
            self.parent.destroy()

    def open_file(self):#Open file comand for if the user selects the ability to open a file, displays a window for them to chose the file they want to select
        chosen_file = filedialog.askopenfilename(filetypes=(("Python files", "*.py"),
                                                            ("html Files", "*.html"),
                                                            ("Text files", "*.txt"),
                                                            ("All files", "*.*") ))

        if chosen_file:
                        self.file_chosen.set(chosen_file)
                        self.filesize.set("SIZE: {}".format(os.stat(chosen_file).st_ctime))
                        my_time = time.asctime(time.localtime(os.stat(chosen_file).st_ctime))
                        self.createdate.set("CREATED: {}".format(my_time))

        self.file_chosen.set(chosen_file)
        with open(self.file_chosen.get(), "r") as text_input:
            file_contents = text_input.read()
        self.text1.insert(INSERT, file_contents)
        self.text1["state"] = "disable"


    def about(self):#If the user selects about displays message giving details about the program
        if messagebox.askokcancel("About", "Created in Python\n :)\n23/04/2015"):
            pass


def main():#Main function to call functions and create gooey
    root = Tk()
    root.wm_title("Lab test 2015, Program to open files")
    GUI(root)
    root.mainloop()


if __name__ == '__main__':#start program
    main()
