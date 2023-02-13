from tkinter import *
from  tkinter import ttk

class  text_editor(Tk):
    def __init__(self):
        #setting
        super().__init__()
        self.title("TextEditor")
        self.geometry("{}x{}".format(400,500))
        #this functino make menu bar
        self.menu=self.menu_bar()
        self.text=self.text_space()

    def menu_bar(self):
        #make menubar for main window
        menubar=Menu(self)
        #add menu bar to window
        self.configure(menu=menubar)
        #make items of menu bar
        file=Menu(menubar,tearoff=0,activeborderwidth=2)
        edit= Menu(menubar, tearoff=0)
        format_= Menu(menubar, tearoff=0)
        help_= Menu(menubar, tearoff=0)
        #add items in menu bar
        menubar.add_cascade(menu=file,label="file")
        menubar.add_cascade(menu=edit, label="edit")
        menubar.add_cascade(menu=format_, label="format")
        menubar.add_cascade(menu=help_, label="help")
        #add item to file item
        file.add_command(label="New",command=None,accelerator="Ctrl+N")
        file.add_command(label="open..", command=None,accelerator="Ctrl+O")
        file.add_command(label="Save", command=None,accelerator="Ctrl+S")
        file.add_command(label="SaveAs", command=None)
        file.add_command(label="PageSetup", command=None)
        file.add_command(label="print", command=None,accelerator="Ctrl+P")
        #make line between items
        file.add_separator()
        file.add_command(label="Exit", command=None)
        #add item to edit item
        edit.add_command(label="undo",command=None,accelerator="Ctrl+Z")
        edit.add_separator()
        edit.add_command(label="cut", command=None, accelerator="Ctrl+X")
        edit.add_command(label="copy", command=None, accelerator="Ctrl+C")
        edit.add_command(label="paste", command=None, accelerator="Ctrl+V")
        edit.add_command(label="delete", command=None, accelerator="del")
        edit.add_command(label="find", command=None, accelerator="Ctrl+F")
        edit.add_command(label="replace", command=None, accelerator="Ctrl+H")
        edit.add_command(label="goto..", command=None, accelerator="Ctrl+G")
        edit.add_command(label="SelectAll", command=None, accelerator="Ctrl+A")
        edit.add_command(label="timedate", command=None, accelerator="        F5")
        #add item to format item
        format_.add_command(label="font",command=None)
        format_.add_command(label="tag", command=None)
        format_.add_command(label="textcolor", command=None)
        format_.add_command(label="wrap",command=None)

        #add item to help item
        help_.add_command(label="help",command=None)
        help_.add_separator()
        help_.add_command(label="about..",command=None)
        return menubar
    def text_space(self):
        fram=Frame(self)
        fram.pack(expand=True,fill=BOTH)
        text = Text(fram, width=400, height=500,wrap=NONE)
        xbar = ttk.Scrollbar(fram, orient=HORIZONTAL,command=text.xview)
        xbar.pack(side="bottom",fill=X,anchor="s")
        yscrollbar = ttk.Scrollbar(fram,command=text.yview)
        yscrollbar.pack(side="right", fill=Y, anchor="nw")
        text.pack()
        text.configure(xscrollcommand=xbar.set,yscrollcommand=yscrollbar.set)

        return text










if __name__ == "__main__":
    app=text_editor()
    app.mainloop()

