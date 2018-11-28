import xlwt
import xlrd
from xlutils.copy import copy
ans = 'Y'
while ans == 'Y':

    rb = xlrd.open_workbook('PoeDrops.xls')
    wb = copy(rb)
    w_sheet = wb.get_sheet(0)
    file1 = open('checker.txt','r') #autocheck
    print(file1.read())

    a = input('Map number: ')

    b = int(a)
    c = b + 1
    d = str(c)
    cards = input('Cards: ')
    exalts=input('Exalts: ')
    chaos =input('Chaos: ')
    fuses =input('Fuses: ')
    jews = input('Jews: ')
    returns = input('Returns: ')
    misc = input('Misc: ')
    reroll = input('Reroll: ')

    w_sheet.write(b,0,a)
    w_sheet.write(b,1,cards)
    w_sheet.write(b,2,exalts)
    w_sheet.write(b,3,chaos)
    w_sheet.write(b,4,fuses)
    w_sheet.write(b,5,jews)
    w_sheet.write(b,6,returns)
    w_sheet.write(b,7,misc)
    w_sheet.write(b,8,reroll)
    wb.save('PoeDrops.xls')

    print('map',a,'saved')
    open('checker.txt', 'w').close()
    file = open('checker.txt','w')
    file.write('Last Map completed:')
    file.write(a)
    #creates autochecker and manual checker
    file.close()
    ans = input('Would You like to add values again?Y/N:')
