import sys
from tkinter import *
from pytube import YouTube

from tkinter import scrolledtext

window = Tk()

window.geometry('1080x720')
window.title("pytube-ui")

lbl = Label(window, text="URL:")
lbl.grid(column=0, row=0)

lbl = Label(window, text="iTag:")
lbl.grid(column=0, row=2)

txt2 = Entry(window,width=30)
txt2.grid(column=1, row=2)

txt = Entry(window,width=30)
txt.grid(column=1, row=0)



def clicked():
    res=txt.get()
    yt = YouTube(res)
    
    txt1 = scrolledtext.ScrolledText(window,width=80,height=60)
    txt1.grid(column=3,row=3)
    txt1.insert(INSERT,yt.streams.all())
    itg=txt2.get()
    itg= int(itg)
    stream = yt.streams.get_by_itag(itg)
    stream.download()
    lbl.configure(text="Downloading...")



btn = Button(window, text="Downlad Video", command=clicked)
btn.grid(column=2, row=0)
window.mainloop()
