import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('PoeDrops.csv')
df
#maps in relation to certain drops:
ansre = 'Y'
while ansre == 'Y':

    print("""
    1.Chaos
    2.Card
    3.Exalt
    4.Fuses
    5.Jews
    6.Returns
    7.MiscDrops
    8.All
    """)

    plotans = input('Which currency do you want to get info on(1-8): ')
    to_grp = [df.index.any]
    if plotans == '1':
        df.plot.line(y= 'Chaos',x ='Map#')
        df.plot.box(y='Chaos',x='Map#')
        grp = df.groupby(to_grp,squeeze = True)['Chaos'].agg(['min', 'mean', 'max'])
        print(grp.head())
        plt.show()
    if plotans =='2':
        df.plot(y = 'Card',x ='Map#')
        grp = df.groupby(to_grp)['Card'].agg(['min', 'mean', 'max'])
        df.plot.box(y='Card',x='Map#')
        print(grp.head())
        plt.show()
    if plotans =='3':
        df.plot(y = 'Exalt',x ='Map#')
        df.plot.box(y='Exalt',x='Map#')
        grp = df.groupby(to_grp)['Exalt'].agg(['min', 'mean', 'max'])
        print(grp.head())

        plt.show()

    if plotans =='4':
        df.plot(y = 'Fuses',x ='Map#')
        df.plot.box(y='Fuses',x='Map#')
        grp = df.groupby(to_grp)['Fuses'].agg(['min', 'mean', 'max'])
        print(grp.head())
        plt.show()
    if plotans =='5':
        df.plot(y = 'Jews',x ='Map#')
        df.plot.box(y='Jews',x='Map#')
        grp = df.groupby(to_grp)['Card'].agg(['min', 'mean', 'max'])
        print(grp.head())
        plt.show()
    if plotans == '6':
        df.plot(y = 'Returns',x ='Map#')
        df.plot.box(y='Returns',x='Map#')
        grp = df.groupby(to_grp)['Returns'].agg(['min', 'mean', 'max'])
        print(grp.head())
        plt.show()
    if plotans == '7':
        df.plot(y = 'MiscDrops',x ='Map#')
        grp = df.groupby(to_grp)['MiscDrops'].agg(['min', 'mean', 'max'])
        print(grp.head())
        plt.show()
    if plotans == '8':
        df.plot.line(x= 'Map#')
        plt.show()
    ansre = input('Would you like to check any other currency?(Y/N)')
    
