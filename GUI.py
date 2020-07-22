from tkinter import *
from tkinter.ttk import *
from Download import Download
import math

class GUI(Frame):

    def __init__(self, master=None):
        self.urls = []

        Frame.__init__(self, master, width=800, height=500)
        self.master.title("Not Illegal Youtube Downloader")
        self.master.bind('<Return>', self.enter_key)
        self.pack(side=RIGHT, fill=BOTH)

        #URL Label
        self.label = Label(master, text="URL")
        self.label.place(relx=0.1,rely=0.1)
        
        #URL Entry form
        self.url_entry = Entry(master, width="90")
        self.url_entry.place(relx=0.2,rely=0.1)

        #Enter Button, when this button is pressed, user entered url will be added to self.urls

        self.button_enter = Button(master, command=self.enter_button_click ,text="Enter")
        self.button_enter.place(relx=0.9,rely=0.1)

        #url listbox
        self.url_listbox = Listbox(master, selectmode=SINGLE, width="110", height="18")
        self.url_listbox.place(relx=0.1, rely=0.2)

        self.button_download = Button(master,command=self.download_button_click, text="Download")
        self.button_download.place(relx=0.9, rely=0.9)

        self.button_reset = Button(master, command=self.reset_button_click, text="Reset")
        self.button_reset.place(relx=0.8, rely=0.9)

        #progess bar
        self.progress = Progressbar(master, orient = HORIZONTAL, length=665, mode='determinate')
        self.progress.place(relx=0.1, rely=0.8)

    def enter_key(self, event):
        self.enter_button_click()

    def enter_button_click(self):
        temp_url = self.url_entry.get()
        self.urls.append(temp_url)
        self.clear_entry()
        self.refresh_listbox()
        print(self.urls)

    #refresh listbox when item is added or deleted, (probably a better way to implement)
    def refresh_listbox(self):
        #clear list box
        self.url_listbox.delete(0,END)
        
        #iterate through self.urls and insert each entry to listbox 
        for url in self.urls:
            self.url_listbox.insert(END, url)

    #takes list of urls and downloads mp3
    def download_button_click(self):
        
        download = Download()
        
        progress_step = int((100.0/len(self.urls)))
        prog=0
        for index, url in enumerate(self.urls):
            self.master.update()
            download.download_url(url)
            prog += progress_step
            print(prog)
            self.progress['value'] = prog
        self.progress['value'] = 100

    def reset_button_click(self):
        print("reset button clicked")
        self.urls = []
        self.progress['value']=0
        self.refresh_listbox()
        self.master.update()
                
    # Delete the url entry when "Enter" button is pressed
    def clear_entry(self):
        self.url_entry.delete(0, 'end')


if __name__ == "__main__":
    guiFrame = GUI()
    guiFrame.mainloop()

