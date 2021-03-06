import tkinter as Tkinter
from tkinter import *
import csv
import xlsxwriter
import pandas as pd
from tkinter.messagebox import showinfo

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.output()

    def output(self):
        Label(text='Chaos:').pack(side=LEFT,padx=5,pady=5)
        self.e = Entry(root, width=5)
        self.e.pack(side=LEFT,padx=5,pady=5)
        Label(text='Fuses:').pack(side=LEFT,padx=5,pady=5)
        self.f = Entry(root, width=5)
        self.f.pack(side=LEFT,padx=5,pady=5)
        Label(text='Jews:').pack(side=LEFT,padx=5,pady=5)
        self.j = Entry(root, width=5)
        self.j.pack(side=LEFT,padx=5,pady=5)
        Label(text='Card:').pack(side=LEFT,padx=5,pady=5)
        self.c = Entry(root, width=5)
        self.c.pack(side=LEFT,padx=5,pady=5)
        Label(text='Exalt:').pack(side=LEFT,padx=5,pady=5)
        self.ex = Entry(root, width=5)
        self.ex.pack(side=LEFT,padx=5,pady=5)
        Label(text='Misc:').pack(side=LEFT,padx=5,pady=5)
        self.m = Entry(root, width=5)
        self.m.pack(side=LEFT,padx=5,pady=5)
        Label(text='Reroll:').pack(side=LEFT,padx=5,pady=5)
        self.r = Entry(root, width=5)
        self.r.pack(side=LEFT,padx=5,pady=5)
        Label(text='Returns:').pack(side=LEFT,padx=5,pady=5)
        self.ret=Entry(root, width = 5)
        self.ret.pack(side=LEFT,padx=5,pady=5)
        self.b = Button(root, text='Submit', command=self.writeToFile)
        self.b.pack(side=LEFT,padx=5,pady=5)

    def writeToFile(self):
        with open('PoeDrops.csv', 'a') as f:
            w=csv.writer(f)
            w.writerow([self.e.get(),self.f.get(),self.j.get(),self.c.get(),self.ex.get(),self.m.get(),self.r.get(),self.ret.get()])
            showinfo("Confirmation", "Submited")


if __name__ == "__main__":
    root=Tk()
    root.title('PoE Map Data Gatherer')
    root.geometry('850x100')
    app=App(master=root)
    root.iconbitmap('mmokico.ico')
    app.mainloop()
    root.mainloop()
