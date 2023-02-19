from tkinter import *
from  tkinter import ttk
from tkinter import  filedialog
from tkinter import  messagebox
import os
import datetime
from tkinter import colorchooser

class  text_editor(Tk):
    def __init__(self):
        #setting
        super().__init__()
        self.title("TextEditor")
        self.geometry("{}x{}".format(400,500))
        #this functino make menu bar
        self.name=StringVar()
        self.src_file=StringVar()
        self.fram = Frame(self).pack(expand=True, fill=BOTH)
        self.menu=self.menu_bar()
        self.text=self.text_space()
        self.name.set("NUL")
        self.wrap_var=IntVar()
        self.wrap_var.set(1)
        self.protocol("WM_DELETE_WINDOW",self.close_root_page)
        self.binding=self.binding_function()
        self.pop_up=self.popup_menue()


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
        file.add_command(label="New",command=self.new_item,accelerator="Ctrl+N")
        file.add_command(label="open..", command=self.open_item,accelerator="Ctrl+O")
        file.add_command(label="Save", command=self.save_item,accelerator="Ctrl+S")
        file.add_command(label="SaveAs", command=self.save_as_item)
        file.add_command(label="print", command=self.print_item,accelerator="Ctrl+P")
        #make line between items
        file.add_separator()
        file.add_command(label="Exit", command=self.exit_item)
        #add item to edit item
        edit.add_command(label="undo",command=self.undo_item,accelerator="Ctrl+Z")
        edit.add_separator()
        edit.add_command(label="cut", command=self.cut_item, accelerator="Ctrl+X")
        edit.add_command(label="copy", command=self.copy_item, accelerator="Ctrl+C")
        edit.add_command(label="paste", command=self.paste_item, accelerator="Ctrl+V")
        edit.add_command(label="delete", command=self.delete_item, accelerator="del")
        edit.add_command(label="find", command=self.find_item, accelerator="Ctrl+F")
        edit.add_command(label="replace", command=self.replace_item, accelerator="Ctrl+H")
        edit.add_command(label="goto..", command=self.go_to_line_item, accelerator="Ctrl+G")
        edit.add_command(label="SelectAll", command=self.select_all_item, accelerator="Ctrl+A")
        edit.add_command(label="timedate", command=self.date_time_item, accelerator="        F5")
        #add item to format item
        format_.add_command(label="font",command=self.font_item)
        format_.add_command(label="textcolor", command=self.text_color_item)
        format_.add_command(label="wrap",command=self.wrap_item)

        #add item to help item
        help_.add_command(label="help",command=self.help_item)
        help_.add_separator()
        help_.add_command(label="about..",command=self.about_item)
        return menubar
    def text_space(self):
        text = Text(self.fram, width=400, height=500,wrap=NONE,undo=True)
        xbar = ttk.Scrollbar(self.fram, orient=HORIZONTAL,command=text.xview)
        xbar.pack(side="bottom",fill=X,anchor="s")
        yscrollbar = ttk.Scrollbar(self.fram,command=text.yview)
        yscrollbar.pack(side="right", fill=Y, anchor="nw")
        text.pack()
        text.configure(xscrollcommand=xbar.set,yscrollcommand=yscrollbar.set)
        return text
    def error_handler(self,msg):
        if msg == "error":
            messagebox.showerror("error","some thing is wrong")
        elif msg =='selection_error':
            messagebox.showinfo("selection","you must select some thing then use this widget")

    def close_root_page(self):
        if len(self.text.get("1.0", "end-1c")) > 0 and self.name.get() == "NUL":
            msg = messagebox.askyesno("save", "do you want save you're file?")
            if msg:
                src = filedialog.asksaveasfilename()
                if src:
                    try:
                        name = src.split("/")[-1]
                        with open(src, "w") as f:
                            f.write(self.text.get("1.0", "end-1c"))
                        self.name.set(name)
                        self.src_file.set(src)
                        self.title(name)
                        self.destroy()
                    except:
                        self.error_handler("error")
            else:
                self.destroy()
        elif self.name.get() != "NUL":
            src = self.src_file.get()
            with open(src, "r") as f:
                text = f.read()
            data = self.text.get("1.0", "end-1c")
            if data == text:
                self.destroy()
            else:
                msg = messagebox.askyesno("save", "do you want save you're file?")
                if msg:
                    with open(src, "w") as f:
                        f.write(data)
                    self.destroy()
                else:
                    self.destroy()
        else:
            self.destroy()

    def new_item(self,event=None):
        self.text.delete("1.0",END)
        self.title("Untitle")
        self.name.set("NUL")
    def open_item(self,event=None):
        def inner_open():
            filetypes = (('text files', '*.txt'), ('python files', '*.py'), ('All files', '*.*'))
            src = filedialog.askopenfilename(filetypes=filetypes)
            if src:
                try:
                    name = src.split("/")[-1]
                    with open(src, "r") as f:
                        text = f.read()
                    self.text.delete("1.0", END)
                    self.text.insert("1.0", text)
                    self.name.set(name)
                    self.src_file.set(src)
                    self.title(name)
                except:
                    self.error_handler("error")

        name = self.name.get()
        src = self.src_file.get()
        if name != "NUL":
            with open(src, "r") as f:
                text = f.read()
            data = self.text.get("1.0", "end-1c")
            if data == text:
                inner_open()
            else:
                msg=messagebox.askyesno("save","do you want save this file?")
                if msg:
                    with open(src,"w") as f:
                        f.write(self.text.get("1.0","end-1c"))
                    inner_open()
                else:
                    inner_open()
        else:
            inner_open()



    def save_item(self,event=None):
        name=self.name.get()
        src=self.src_file.get()
        if name == "NUL":
            src = filedialog.asksaveasfilename()
            if src:
                try:
                    name = src.split("/")[-1]
                    with open(src, "w") as f:
                        f.write(self.text.get("1.0", "end-1c"))
                    self.name.set(name)
                    self.src_file.set(src)
                    self.title(name)
                except:
                    self.error_handler("error")
        else:
            try:
                name = src.split("/")[-1]
                with open(src, "w") as f:
                    f.write(self.text.get("1.0", "end-1c"))
                self.name.set(name)
                self.src_file.set(src)
                self.title(name)
            except:
                self.error_handler("error")



    def save_as_item(self):
        src = filedialog.asksaveasfilename()
        if src :
            try:
                name = src.split("/")[-1]
                with open(src, "w") as f:
                    f.write(self.text.get("1.0", "end-1c"))
                self.name.set(name)
                self.src_file.set(src)
                self.title(name)
            except:
                self.error_handler("error")
    def print_item(self,event=None):
        src=self.src_file.get()
        try:
           os.startfile(src, "print")
        except:
           self.error_handler("error")
    def exit_item(self):
        name=self.name.get()
        src=self.src_file.get()
        if name == "NUL":
            msg = messagebox.askyesno("save", "do you want save your file?")
            if msg:
                self.save_item()
                self.destroy()
            else:
                self.destroy()
        else:
            try:
                with open(src, "r") as f:
                    text = f.read()
                data = self.text.get("1.0", "end-1c")
                if text == data:
                    self.destroy()
                else:
                    msg = messagebox.askyesno("save", "do you want save your file?")
                    if msg:
                        try:
                            data = self.text.get("1.0", "end-1c")
                            with open(src,"w") as f:
                                f.write(data)
                            self.destroy()
                        except:
                            self.error_handler("error")
                        self.destroy()
                    else:
                        self.destroy()
            except:
                self.error_handler("error")

    def cut_item(self):
        try:
            value = self.text.selection_get()
            self.text.delete("sel.first", "sel.last")
            self.clipboard_clear()
            self.clipboard_append(value)
        except:
            self.error_handler("selection_error")


    def copy_item(self):
        try:
            value = self.text.selection_get()
            self.clipboard_clear()
            self.clipboard_append(value)
        except:
            self.error_handler("selection_error")
    def paste_item(self):
        try:
            value=self.clipboard_get()
            self.text.insert("insert",value)
        except:
            self.error_handler("error")
    def delete_item(self):
        try:
            # value=self.text.selection_get()
            self.text.delete("sel.first", "sel.last")
        except:
            self.error_handler("selection_error")
    def find_item(self,event=None):
        global entry_find
        def find_close_function():
            self.text.tag_remove('found', '1.0', END)
            root.destroy()
        root=Toplevel(self)
        root.title("find")
        root.geometry("250x70")
        root.resizable(height=False,width=False)
        fram=Frame(root,width=240,height=90)
        fram.pack()
        entry_find=Entry(fram,width=40)
        entry_find.pack(side="top",pady=10)
        btn=Button(fram,text="find", width=8,height=1,command=self.find_item_btn)
        btn.pack(side="top",padx=10)
        root.protocol("WM_DELETE_WINDOW",find_close_function)
    def find_item_btn(self):
        self.text.tag_remove('found', '1.0', END)
        key=entry_find.get()
        if key:
            idx = '1.0'
            while True:
                idx = self.text.search(key, idx, nocase=1, stopindex=END)
                if not idx: break
                lastidx = '%s+%dc' % (idx, len(key))
                self.text.tag_add('found', idx, lastidx)
                idx = lastidx
                self.text.see(idx)
            self.text.tag_config('found', background='yellow')
    def replace_item(self,event=None):
        global entry_word
        global entry_replace
        root=Toplevel(self)
        root.geometry("250x150")
        root.title("replace")
        root.resizable(height=False,width=False)
        Label(root,text="find what:").pack(side="top",anchor="w")
        entry_word=Entry(root,width=35,font=("Arial",10))
        entry_word.pack(side="top",pady=10)
        Label(root, text="replace with:").pack(side="top",anchor="w")
        entry_replace= Entry(root, width=40,font=("Arial",10))
        entry_replace.pack(side="top",pady=10)
        btn_replace=Button(root,text="replace",command=self.replace_item_btn)
        btn_replace.pack(side="top",anchor="center")
    def replace_item_btn(self):
        word=entry_word.get()
        replace=entry_replace.get()
        if word:
            idx = '1.0'
            while True:
                idx = self.text.search(word, idx, nocase=1, stopindex=END)
                if not idx: break
                lastidx = '%s+%dc' % (idx, len(word))
                self.text.tag_add('found', idx, lastidx)
                self.text.replace("found.first", "found.last", replace)
                idx = lastidx
                self.text.see(idx)
    def go_to_line_item(self,event=None):
        global entry_go_to
        root=Toplevel(self)
        root.geometry("270x70")
        root.resizable(height=False,width=False)
        root.title("GoToLine")
        Label(root,text="go to line:").pack(side="left",anchor="w",padx=5)
        entry_go_to=Entry(root,width=18,font=("Arial",10))
        entry_go_to.pack(side="left",anchor="center")
        btn=Button(root,text="Go",width=7,command=self.go_to_line_btn)
        btn.pack(side="left",anchor="e",padx=8)
    def go_to_line_btn(self):
        var=entry_go_to.get()
        self.text.mark_set(INSERT, float(var))
    def select_all_item(self):
        end = int(self.text.index("end")[0])
        for i in range(end + 1):
            self.text.tag_add("selection", f"{i}.0", f"{i}.0 lineend")
        self.text.tag_configure('selection', background="#3399FF", foreground="white")

    def bind_select(self,event):
        self.text.tag_remove('selection', '1.0', END)
    def date_time_item(self,event=None):
        x = datetime.datetime.now()
        frame=x.strftime("%H:%M %p %x")
        self.text.insert("insert",frame)
    def list_of_font(self):
        list_= os.listdir(r'C:\Windows\fonts')
        output=[]
        for i in list_:
            output.append(i.split(".")[0])
        return output

    def font_item(self):
        global font_var
        global style_var
        global size_var
        global font_toplevel
        root=Toplevel(self)
        root.geometry("400x200")
        root.resizable(height=False,width=False)
        root.title("font")
        main_frame=Frame(root,width=390,height=180)
        main_frame.pack(side="top")
        fram=Frame(main_frame,width=100,height=100)
        fram.pack(side="left",pady=50)
        fram_1 = Frame(main_frame, width=100, height=100, )
        fram_1.pack(side="left", pady=50)
        fram_2= Frame(main_frame, width=390, height=100, )
        fram_2.pack(side="left", pady=50)
        font_var=StringVar()
        size_var=IntVar()
        style_var=StringVar()
        list_of_font=self.list_of_font()
        lable_font=Label(fram,text="font:")
        lable_font.pack(side="top")
        font_combo_box=ttk.Combobox(fram,textvariable=font_var,width=20)
        font_combo_box.pack(side="top",padx=10)
        font_combo_box["values"]=tuple(list_of_font)
        lable_style = Label(fram_1, text="style:")
        lable_style.pack(side="top")
        style_combo_box = ttk.Combobox(fram_1, textvariable=style_var, width=15)
        style_combo_box.pack(side="top",padx=10)
        style_combo_box["values"]=("bold","italic","underline","underline")
        lable_size = Label(fram_2, text="size:")
        lable_size.pack(side="top")
        size_spinbox=ttk.Spinbox(fram_2,from_=1,to=100,textvariable=size_var,width=8)
        size_spinbox.pack(side="top",padx=10)
        #---------------------------------------------------
        btn_cancle = Button(root, text="cancle", width=7, height=1, command=lambda : root.destroy())
        btn_cancle.pack(side="right", pady=10, padx=5)
        btn_ok=Button(root,text="ok",width=7,height=1,command=self.font_item_btn_set)
        btn_ok.pack(side="right",pady=10,padx=5)
        font_toplevel=root
    def font_item_btn_set(self):
        font=font_var.get()
        style=style_var.get()
        size=size_var.get()
        self.text.configure(font=(font,size,style))
        font_toplevel.destroy()
    def text_color_item(self):
        color=colorchooser.askcolor(initialcolor="#FFFFFF")
        self.text.configure(foreground=color[1])
    def wrap_item(self):
        var=self.wrap_var.get()
        if var:
            self.text.configure(wrap="word")
            self.wrap_var.set(0)
        else:
            self.text.configure(wrap="none")
            self.wrap_var.set(1)
    def help_item(self):
        root=Toplevel(self)
        root.geometry("400x200")
        root.resizable(height=False,width=False)
        root.title("help")
        fram=LabelFrame(root,width=390,height=190,text="help")
        fram.pack(side="top",ipadx=40)
        txt="""
        this help of text texteditor in format menu \n
        we have wrap this option diactive xscrollbarand\n 
        make wrap word in this version font and textcolor\n
         just chnge iner face ofthis app and we can save\n
          this change.
        """
        lable=Label(fram,text=txt,justify="left")
        lable.pack(side="top",anchor="center")
    def about_item(self):
        root = Toplevel(self)
        root.geometry("400x200")
        root.resizable(height=False, width=False)
        root.title("about")
        fram = LabelFrame(root, width=390, height=190, text="about")
        fram.pack(side="top",ipady=20,ipadx=50)
        txt = """
        this is text editor write by python language\n
        and make with tkinter library \n
                            amir mollaiee
             """
        lable = Label(fram, text=txt, justify="left")
        lable.pack(side="top", anchor="center")
    def undo_item(self,event=None):
        try:
            self.text.edit_undo()
        except:
            pass
    def binding_function(self):
        self.text.bind("<ButtonPress-1>", self.bind_select)
        self.text.bind("<ButtonPress-3>", self.bind_select)
        self.bind("<Control-N>",self.new_item)
        self.bind("<Control-n>", self.new_item)
        self.bind("<Control-O>", self.open_item)
        self.bind("<Control-o>", self.open_item)
        self.bind("<Control-S>", self.save_item)
        self.bind("<Control-s>", self.save_item)
        self.bind("<Control-P>", self.print_item)
        self.bind("<Control-p>", self.print_item)
        self.bind("<Control-F>", self.find_item)
        self.bind("<Control-f>", self.find_item)
        self.bind("<Control-H>", self.replace_item)
        self.bind("<Control-h>", self.replace_item)
        self.bind("<Control-G>", self.go_to_line_item)
        self.bind("<Control-g>", self.go_to_line_item)
        self.bind("<Control-H>", self.replace_item)
        self.bind("<F5>", self.date_time_item)
        self.bind("<Button-3>", self.menu_popup)
    def popup_menue(self):
        popup = Menu(self, tearoff=0,)
        popup.add_command(label=" undo           ",command=self.undo_item)
        popup.add_separator()
        popup.add_command(label=" cut           ", command=self.cut_item)
        popup.add_command(label=" copy           ", command=self.copy_item)
        popup.add_command(label=" paste           ", command=self.paste_item)
        popup.add_command(label=" Delete           ", command=self.delete_item)
        popup.add_separator()
        popup.add_command(label=" select_all          ", command=self.select_all_item)

        return popup

    def menu_popup(self,event):
        popup=self.pop_up
        try:
            popup.tk_popup(event.x_root, event.y_root, 0)
        finally:
            popup.grab_release()


if __name__ == "__main__":
    app=text_editor()
    app.mainloop()

