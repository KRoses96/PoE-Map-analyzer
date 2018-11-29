print('Welcome to the PoE map analyzer')
print("""Menu:
        1.Updater
        2.Analyzer
        3.Update Ratios
        4.Exit""")

ansmain2 = 'Y'
while ansmain2 == 'Y':
    ansmain = input('What would you like to do(1-4): ')
    if ansmain == '1':
        import updater
        ansmain2 = input('Would you like to back to the main menu(Y/N):')
    if ansmain == '2':
        import converter
        import analyzer
        ansmain2 = input('Would you like to back to the main menu(Y/N):')
    if ansmain == '3':
        import ratios
    elif ansmain == '4':
        print('Thanks for using the analyzer')
        break
