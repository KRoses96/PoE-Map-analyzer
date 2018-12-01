import pandas as pd
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('PoeDrops.csv')
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

valm = df['Misc'].sum()

valre = df['Reroll'].sum()

supersum = valcdr + valjr +valm +valc +valer


#Def used to highlight mins and maxs in table9
def highlight_max(data, color='green'):
    '''
    highlight the maximum in a Series or DataFrame
    '''
    attr = 'background-color: {}'.format(color)
    if data.ndim == 1:  # Series from .apply(axis=0) or axis=1
        is_max = data == data.max()
        return [attr if v else '' for v in is_max]
    else:  # from .apply(axis=None)
        is_max = data == data.max().max()
        return pd.DataFrame(np.where(is_max, attr, ''),
                            index=data.index, columns=data.columns)
def highlight_min(data, color='red'):
    '''
    highlight the min in a Series or DataFrame
    '''
    attr = 'background-color: {}'.format(color)
    if data.ndim == 1:  # Series from .apply(axis=0) or axis=1
        is_max = data == data.min()
        return [attr if v else '' for v in is_max]
    else:  # from .apply(axis=None)
        is_max = data == data.max().max()
        return pd.DataFrame(np.where(is_max, attr, ''),
                            index=data.index, columns=data.columns)
#
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
    9.Tables
    """)

    plotans = input('What data do you want to check (1-9): ')
    to_grp = [df.index.any]
    if plotans == '1':
        #chaos information
        df.plot.line(y= 'Chaos')
        df.plot.box(y='Chaos')
        grp = df.groupby(to_grp,squeeze = True)['Chaos'].agg(['min', 'mean', 'max'])
        print(grp.head())
        plt.title('Chaos')
        plt.show()
    if plotans =='2':
        #card information
        c1=df.plot(y = 'Card')
        grp = df.groupby(to_grp)['Card'].agg(['min', 'mean', 'max'])
        c2=df.plot.box(y='Card')
        print(grp.head())
        plt.show()
    if plotans =='3':
        #exalt information
        df.plot(y = 'Exalt')
        df.plot.box(y='Exalt')
        grp = df.groupby(to_grp)['Exalt'].agg(['min', 'mean', 'max'])
        print(grp.head())

        plt.show()

    if plotans =='4':
        #fuses information
        df.plot(y = 'Fuses')
        df.plot.box(y='Fuses')
        grp = df.groupby(to_grp)['Fuses'].agg(['min', 'mean', 'max'])

        plt.show()
    if plotans =='5':
        #jew information
        df.plot(y = 'Jews')
        df.plot.box(y='Jews')
        grp = df.groupby(to_grp)['Jews'].agg(['min', 'mean', 'max'])
        print(grp.head())
        plt.show()
    if plotans == '6':
        #Shows Returns information
        df.plot(y = 'Returns')
        df.plot.box(y='Returns')
        grp = df.groupby(to_grp)['Returns'].agg(['min', 'mean', 'max'])
        print(grp.head())
        plt.show()
    if plotans == '7':
        #shows info on misc drops
        df.plot(y = 'Misc')
        grp = df.groupby(to_grp)['Misc'].agg(['min', 'mean', 'max'])
        print(grp.head())
        plt.show()
    if plotans == '8':
        #shows info on all
        df.plot.line()
        plt.show()
    if plotans == '9':
        plotansanswh = 'Y'
        while plotansanswh == 'Y':
            print("""Menu:
            1.Major losses
            2.Major gains""")
            plotansans = input('Which table would you like to choose?')
            if plotansans == '1':
                dfred =df.style.apply(highlight_min)
                dfred
                plotansanswh = input('Would you like to check more tables?(Y/N) ')
            if plotansans == '2':
                dfgrn =df.style.apply(highlight_max)
                dfgrn
                plotansanswh = input ('Would you like to check more tables?(Y/N)')
    ansre = input('Would you like to check any other data?(Y/N)')
