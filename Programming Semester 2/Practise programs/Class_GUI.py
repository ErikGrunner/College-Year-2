__author__ = 'Ciaran O Loughlin'

from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox
import os


class GUI():
    def __init__(self, parent):
        self.parent = parent
        self.parent.protocol("WM_DELETE_WINDOW", self.catch_destroy)

        self.parent.option_add("*tearOff", FALSE)

        self.menu = Menu(self.parent)
        self.file_menu = Menu(self.menu)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.catch_destroy)

        self.help_menu = Menu(self.menu)
        self.help_menu.add_command(label="About", command=self.about)

        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.parent.config(menu=self.menu)

        self.frame1 = ttk.Frame(self.parent, padding=5, border=1)
        self.frame1.grid(row=0, column=0)

        self.file_chosen = StringVar()
        self.label1 = ttk.Label(self.frame1, text="test")
        self.label1.grid(row=0, column=0, sticky=W+E)

        self.text1 = Text(self.frame1, width=100, wrap=NONE)
        self.text1.grid(row=1, column=0)

        self.yscroll = ttk.Scrollbar(self.frame1, orient=VERTICAL, command=self.text1.yview)
        self.yscroll.grid(row=1, column=1, sticky=N+S)

        self.xscroll = ttk.Scrollbar(self.frame1, orient=HORIZONTAL, command=self.text1.xview)
        self.xscroll.grid(row=2, column=0, sticky=W+E)

        self.text1["yscrollcommand"] = self.yscroll.set
        self.text1["xscrollcommand"] = self.xscroll.set

    def catch_destroy(self):
        if messagebox.askokcancel("Quit", "Do you really want to quit?"):
            self.parent.destroy()

    def open_file(self):
        chosen_file = filedialog.askopenfilename(filetypes=(("Python files", "*.py"),
                                                            ("Text files", "*.txt"),
                                                            ("All files", "*.*") ))
        self.file_chosen.set(chosen_file)
        with open(self.file_chosen.get(), "r") as text_input:
            file_contents = text_input.read()
        self.text1.insert(INSERT, file_contents)
        self.text1["state"] = "disable"

    def about(self):
        if messagebox.askokcancel("About", "Created in Tkinter\n12/03/2015"):
            pass


def main():
    root = Tk()
    root.wm_title("File Opener")
    GUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
