import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('PoeDrops.csv')
df
#maps in relation to certain drops:
ansre = 'Y'
while ansre == 'Y':

    print("""1.Chaos
    2.Card
    3.Exalt
    4.Fuses
    5.Jews
    6.Returns
    7.MiscDrops
    8.All""")

    plotans = input('Which currency do you want to get info on: (1-8)')

    if plotans == '1':
        df.plot(y= 'Chaos',x ='Map#')
    if plotans =='2':
        df.plot(y = 'Card',x ='Map#')
    if plotans =='3':
        df.plot(y = 'Exalt',x ='Map#')
    if plotans =='4':
        df.plot(y = 'Fuses',x ='Map#')
    if plotans =='5':
        df.plot(y = 'Jews',x ='Map#')
    if plotans == '6':
        df.plot(y = 'Returns',x ='Map#')
    if plotans == '7':
        df.plot(y = 'MiscDrops',x ='Map#')
    ansre = input('Would you like to check any other currency?(Y/N)')
