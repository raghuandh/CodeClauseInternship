import pyshorteners
from tkinter import *
import tkinter as tk

window = Tk()
window.geometry("800x600")
window.configure(bg="#B2FFC8")
def shorten_url():
    url=Entry_field.get()

    # Using TinyURL as an example
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(url)
    ans = Label(window, text=short_url, font=('Arial',18,'bold'),bg='#B2FFC8')
    ans.pack(padx=0,pady=20)
    
Label(window, text="Enter the URL to Shorten it", font=('Arial',28,'bold'),bg='#B2FFC8').pack(pady=5)
Entry_field = Entry(window, font=('arial',18),width=30)
Entry_field.pack(padx=0,pady=20)
btn = Button(window,text="shorten",bg="#98FB98",border=1,relief=GROOVE,width=10,height=2,\
    font=('Arial',14,'bold'), command=shorten_url)
btn.pack(padx=0,pady=20)
window.mainloop()