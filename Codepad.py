from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
# functions of new file and others
def newfile():
    global file
    root.title("Untitled-codepad")
    file = NONE
    TextArea.delete(1.0,END)
def openfile():
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),
    ("Text Documents","*.txt")])
    if file=="":
        file=NONE
    else:
        root.title(os.path.basename(file)+"-Codepad")
        TextArea.delete(1.0,END)
        f=open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()


def Savefile():
    global file
    if file==NONE:
        file - asksaveasfilename(initialfile= 'untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),
    ("Text Documents","*.txt")])

        if file=="":
            file - NONE

        else:
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file)+"-Codepad")
    else:
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()

        
def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))
def about():
    showinfo("Codepad","A dark theme codepad for programmers who code in light theme notepad\n\"Person using light theme is racist\"")
def quitapp():
    pass

if __name__ == '__main__':
    root = Tk()
    root.title("Codepad")
    root.configure(background="grey22")
    # root.wm_iconbitmap(bitmap="main.ico")
    root.geometry("644x788")

    # adding text area

    TextArea = Text(root,font="lucida 13",fg="Yellow",bg="grey22")
    TextArea.pack(expand=True,fill=BOTH)
    file = None

    #creating menu bar
    Menubar = Menu(root)
    FileMenu = Menu(Menubar)

    #new file
    FileMenu.add_command(label="New",command=newfile)

    # to open alerady existing file
    FileMenu.add_command(label="Open",command=openfile)
    # save file
    FileMenu.add_command(label="Save",command=Savefile)

    FileMenu.add_separator()
    FileMenu.add_command(label="Exit",command=quitapp)

    Menubar.add_cascade(label="File",menu=FileMenu)
    # edit menu start
    EditMenu = Menu(Menubar,tearoff=0)
    # to give a feature of cut,copy and paste
    EditMenu.add_command(label="Cut",command=cut)
    EditMenu.add_command(label="Copy",command=copy)
    EditMenu.add_command(label="Paste",command=paste)

    Menubar.add_cascade(label="Edit",menu=EditMenu)
    # help menu starts
    HelpMenu = Menu(Menubar,tearoff=0)
    HelpMenu.add_command(label="About Codepad",command=about)
    Menubar.add_cascade(label="About",menu=HelpMenu)



    root.config(menu=Menubar)

    # adding scroll bar right
    Srlbar = Scrollbar(TextArea)
    Srlbar.pack(side=RIGHT,fill=Y)
    Srlbar.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Srlbar.set)
    
    



    root.mainloop()