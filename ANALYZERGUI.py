import tkinter as Tkinter
from tkinter import *
import matplotlib.pyplot as plt
from pandas import read_csv
import plotly.graph_objs as go
df = read_csv('PoeDrops.csv')
#Sums of all values from the csv file
valc = df['Chaos'].sum()

valcd = df['Card'].sum()
valcdr = valcd * 25


vale = df['Exalt'].sum()
valer = vale * 60

valf = df['Fuses'].sum()
valfr = valf * 1/2

valj = df['Jews'].sum()
valjr = valj *1/8
valret = df['Returns'].sum()
valm = df['Misc'].sum()

valre = df['Reroll'].sum()
#supersum is the reason we sum all those numbers before
supersum = valcdr + valjr +valm +valc +valer

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.output()

    def output(self):
        Label(text='Returns:').pack(side=LEFT)
        Label(text=valret).pack(side=LEFT,pady=5)
        Label(text='Reroll:').pack(side=LEFT,pady=5)
        Label(text=valre).pack(side=LEFT,pady=5)
        Label(text='Jews:').pack(side=LEFT,pady=5)
        Label(text=valj).pack(side=LEFT,pady=5)
        Label(text='Fuses:').pack(side=LEFT,pady=5)
        Label(text=valf).pack(side=LEFT,pady=5)
        Label(text='Exalts:').pack(side=LEFT)
        Label(text=vale).pack(side=LEFT,pady=5)
        Label(text='Cards:').pack(side=LEFT,pady=5)
        Label(text=valcd).pack(side=LEFT,pady=5)
        Label(text='Chaos').pack(side=LEFT,pady=5)
        Label(text=valc).pack(side=LEFT,pady=5)
        Label(text='Sum:').pack(side=LEFT,pady=5)
        Label(text=supersum).pack(side=LEFT,pady=5)
        self.bc = Button(root,text='Chaos',command=self.chaosgp)
        self.bc.pack(side=TOP,fill=X)
        self.bf = Button(root,text='Fuses',command=self.fusegp)
        self.bf.pack(side=TOP,fill=X)
        self.bj = Button(root,text='Jews',command=self.jewgp)
        self.bj.pack(side=TOP,fill=X)
        self.bcj = Button(root,text='Cards',command=self.cardgp)
        self.bcj.pack(side=TOP,fill=X)
        self.be = Button(root,text='Exalts',command=self.chaosgp)
        self.be.pack(side=TOP,fill=X)
        self.bm = Button(root,text='Misc',command=self.miscgp)
        self.bm.pack(side=TOP,fill=X)
        self.br = Button(root,text='Returns',command=self.returngp)
        self.bc.pack(side=TOP,fill=X)

    def writeToFile(self):
        with open('PoeDrops.csv', 'a') as f:
            w=csv.writer(f)
            w.writerow([self.e.get(),self.f.get(),self.j.get(),self.c.get(),self.ex.get(),self.m.get(),self.r.get(),self.ret.get()])
    def chaosgp(self):
        df.plot.line(y= 'Chaos')
        df.plot.box(y='Chaos')
        plt.title('Chaos')
        plt.show()
    def chaostat(self):
        grp = df.groupby(to_grp,squeeze = True)['Chaos'].agg(['min', 'mean', 'max'])
        print(grp.head())
        print('Total:')
        print(valc)
    def cardgp(self):
        c1=df.plot(y = 'Card')
        c2=df.plot.box(y='Card')
        plt.show()
    def cardstat(self):
        grp = df.groupby(to_grp)['Card'].agg(['min', 'mean', 'max'])
        print('Total:')
        print(valcdr)
        print(grp.head())
    def exaltgp(self):
        df.plot(y = 'Exalt')
        df.plot.box(y='Exalt')
        plt.show()

    def exaltstat(self):
        grp = df.groupby(to_grp)['Exalt'].agg(['min', 'mean', 'max'])
        print(grp.head())
        print('Total:')
        print(vale)

    def fusegp(self):
        df.plot(y = 'Fuses')
        df.plot.box(y='Fuses')
        plt.show()
    def fusestat(self):
        grp = df.groupby(to_grp)['Fuses'].agg(['min', 'mean', 'max'])
        print('Total:')
        print(valf)

    def jewgp(self):
        df.plot(y = 'Jews')
        df.plot.box(y='Jews')
        plt.show()
    def jewstat(self):
        grp = df.groupby(to_grp)['Jews'].agg(['min', 'mean', 'max'])
        print(grp.head())
        print('Total:')
        print(valj)

    def returngp(self):
        df.plot(y = 'Returns')
        df.plot.box(y='Returns')
        plt.show()
    def returnstat(self):
        grp = df.groupby(to_grp)['Returns'].agg(['min', 'mean', 'max'])
        print(grp.head())
        print('Total:')
        print(valret)

    def miscgp(self):
        df.plot(y = 'Misc')
        plt.show()
    def miscstat(self):
        grp = df.groupby(to_grp)['Misc'].agg(['min', 'mean', 'max'])
        print(grp.head())
        print('Total Chaos Worth Of Misc Drops:')
        print(valm)
    def supersum(self):
        print(supersum)



if __name__ == "__main__":
    root=Tk()
    root.title('PoE Map Analyzer')
    root.geometry('600x156')
    app=App(master=root)
    root.iconbitmap('mmokico.ico')
    app.mainloop()
    root.mainloop()
