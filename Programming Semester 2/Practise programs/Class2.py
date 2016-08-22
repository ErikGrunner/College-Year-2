__author__ = 'Ciaran'
import os, time
from tkinter import *
from tkinter import filedialog, messagebox, ttk

class GUI():
        def __init__(self, parent):
                self.parent = parent
                #self.parent.protocol("WM_DELETE_WINDOW", self.catch_destroy)
                self.parent.option_add("*tearOff", FALSE)
                self.frame = Frame(self.parent, padx="5m", pady="5m")
                self.frame.grid(row=0, column=0)
                self.menu = Menu(self.frame)

                self.file_menu = Menu(self.menu)
                self.file_menu.add_command(label="Open", command=self.open_file)
                self.file_menu.add_separator()
                self.file_menu.add_command(label="Exit", command=self.catch_destroy)

                self.help_menu = Menu(self.menu)
                self.help_menu.add_command(label="About", command=self.about)

                self.menu.add_cascade(label="File", menu=self.file_menu)
                self.menu.add_cascade(label="Help", menu=self.help_menu)
                self.parent.config(menu=self.menu)

                self.filename = StringVar()
                self.filename.set("Filename here")
                self.filelabel = Label(self.frame, textvariable=self.filename)
                self.filelabel.grid(row=0, column=0)

                self.filesize = StringVar()
                self.createdate = StringVar()

                self.datelabel = Label(self.frame, textvariable=self.createdate)
                self.datelabel.grid(row=1, column=0)


        def catch_destroy(self):
                if messagebox.askokcancel("Quit", "Do you really want to quit?"):
                    self.parent.destroy()

        def open_file(self):
                chosen_file = filedialog.askopenfilename(filetypes=(("JPEG", "*.jpg"),
                                                                    ("PNG", "*.png"),
                                                                    ("All files", "*.*") ))
                if chosen_file:
                        self.filename.set(chosen_file)
                        self.filesize.set("SIZE: {}".format(os.stat(chosen_file).st_ctime))
                        my_time = time.asctime(time.localtime(os.stat(chosen_file).st_ctime))
                        self.createdate.set("CREATED: {}".format(my_time))

        def about(self):
                if messagebox.askokcancel("About", "Created in Tkinter\n"):
                    pass

def main():
        root = Tk()
        root.wm_title("File Metadata")
        GUI(root)
        root.mainloop()

if __name__ == '__main__':
	main()
