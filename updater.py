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

    map = input('Map number: ')
    Map_num = int(map)
    cards = input('Cards: ')
    exalts=input('Exalts: ')
    chaos =input('Chaos: ')
    fuses =input('Fuses: ')
    jews = input('Jews: ')
    returns = input('Returns: ')
    misc = input('Misc: ')
    reroll = input('Reroll: ')

    w_sheet.write(Map_num,0,map)
    w_sheet.write(Map_num,1,cards)
    w_sheet.write(Map_num,2,exalts)
    w_sheet.write(Map_num,3,chaos)
    w_sheet.write(Map_num,4,fuses)
    w_sheet.write(Map_num,5,jews)
    w_sheet.write(Map_num,6,returns)
    w_sheet.write(Map_num,7,misc)
    w_sheet.write(Map_num,8,reroll)
    wb.save('PoeDrops.xls')

    print('map',map,'saved')
    open('checker.txt', 'w').close()
    file = open('checker.txt','w')
    file.write('Last Map completed:')
    file.write(map)
    #creates autochecker and manual checker
    file.close()
    ans = input('Would You like to add values again?Y/N:')
