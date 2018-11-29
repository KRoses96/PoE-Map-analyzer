#asks for the ratios for the cards you are farming and exalts
exaltrat = int(input('Exalt ratio: '))
cardrat = int(input('Card ratio: '))

with open('exaltrat.txt', 'w') as f:
    f.write(str(exaltrat))

with open('cardrat.txt','w') as r:
    r.write(str(cardrat))
