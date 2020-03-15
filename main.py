from tkinter import *
from pytube import YouTube

window = Tk()

window.geometry('720x480')
window.title("pytube-ui")

lbl = Label(window, text="URL:")
lbl.grid(column=0, row=0)

txt = Entry(window,width=30)
txt.grid(column=1, row=0)

def clicked():
    res=txt.get()
    yt = YouTube(res)
    stream = yt.streams.first()
    stream.download()
    lbl.configure(text="Downloading...")

btn = Button(window, text="Downlad Video", command=clicked)
btn.grid(column=2, row=0)
window.mainloop()
