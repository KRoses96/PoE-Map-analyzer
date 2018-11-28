import pandas as pd
data_xls = pd.read_excel('PoeDrops.xls', 'Sheet1', index_col=None)
data_xls.to_csv('PoeDrops.csv', encoding='utf-8')
