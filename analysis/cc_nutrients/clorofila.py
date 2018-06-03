'''
Cálculo de clorofila a partir de clorofila.csv
'''

import pandas as pd

data = pd.read_csv('sampling/clorofila.csv', sep=';', index_col=0)

data['formula'] = data['665nm'] - data['750nm']
data['formula2'] = data['665A'] - data['750A']
data['formula3'] = data['formula'] - data['formula2']
data['formula4'] = 11.4*2.43*1.7*data['formula3']*10
data['volume'] = data['volume'] / 1000
data['CC'] = data['formula4'] / data['volume']

data['CC']

data.index
data.columns
data.values

saida4 = data.loc[0:20, ['estacao', 'CC', 'saida']]
saida1 = data.loc[21:37, ['estacao', 'CC', 'saida']]
saida5 = data.loc[38:58, ['estacao', 'CC', 'saida']]

saida4.to_csv('sampling/saida4cc.csv')
saida1.to_csv('sampling/saida1cc.csv')
saida5.to_csv('sampling/saida5cc.csv')
