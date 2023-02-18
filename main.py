import tkinter as tk
from functools import partial
from tkinter.ttk import  *
from tkinter import  *
from pywebcopy import save_website
from datetime import datetime

class Cloner(tk.Tk):

    def __init__(self):
        super(Cloner, self).__init__()
        super(Cloner, self).geometry("400x600")
        super(Cloner, self).config(bg="#6FAFE7")
        super(Cloner, self).title("MINI PYTHON CLONER")
        photo = PhotoImage(file="icon.png")
        super(Cloner, self).iconphoto(False,photo)
        self.contents = tk.StringVar()

        # output folder
        self.output_folder_label = tk.Label(self,width=300, pady=10, text="Output folder",bg="#6FAFE7").pack(side="top")
        self.output_folder = tk.StringVar()
        self.output_folder_entry = tk.Entry(self,width=50, textvariable=self.output_folder).pack(side="top")

        # project name label and text entry box
        self.projectnameLabel = tk.Label(self, width=300, pady=10, text="Project Name", bg="#6FAFE7").pack(side="top")
        self.projectname = tk.StringVar()
        self.projectnameEntry = tk.Entry(self, width=50, textvariable=self.projectname).pack(side="top")

        # url
        self.url_label = tk.Label(self, text="Website Url To Clone",bg="#6FAFE7").pack(side="top")
        self.url = tk.StringVar()
        self.url_entry = tk.Entry(self,width=50, textvariable=self.url).pack(side="top")

        self.do_action = partial(self.GetText, self.output_folder, self.url,self.projectname)
        self.request_button = tk.Button(self, text="Clone",foreground="#fff", background="blue",width=20,command=self.do_action).pack(pady=10)


        # login button

    def quitbtn(self):
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.destroy)
        self.quit.pack(side="bottom")
    def GetText(self,output_folder,url,projectname):
        url = url.get()
        outputfolder =   output_folder.get()
        projectname = projectname.get()
        tk.Label(self, text=f'Cloning Started...\n\n url to clone: {url} \n\n '
                            f'Output Directory:  {outputfolder}\n\nProject Name:  {projectname} \n\n', font=30,
                  pady=10).pack(side="top")
        try:
            save_website(
            url=url,
            project_folder=outputfolder,
            project_name=projectname,
            bypass_robots=True,
            debug=False,
            open_in_browser=True,
            delay=None,
            threaded=False,
            )
        except:
           pass
        tk.Label(self, text="Cloned...",font=30, pady=10,padx=10).pack(side="top")

    # def
    def start(self):
        # self.FolderName()
        # self.Url()
        # self.Clonebtn()
        self.quitbtn()
        super(Cloner, self).mainloop()

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
endingdate =  "25/12/2023 13:31:21"
currentdate = dt_string

if(endingdate > currentdate):
        bank = Cloner()
        bank.start()
else:
    bank = Cloner()
    bank.start()
