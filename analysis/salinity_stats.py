'''
'''

import pandas as pd
from scipy import stats

df = pd.read_csv('data/csv/coordenadas.csv', delimiter = ';')

dsal = df['Surf Sal'] / df['Bot Sal']
data = df['Data']
stations = df['Ponto']
df = pd.DataFrame([dsal, data, stations])
df = df.transpose()
df.columns = ['sal', 'Data', 'Ponto']

ver = df.loc[df['Data'] == '25-Jan-17']
out = df.loc[df['Data'] == '27-May-17']
inv = df.loc[df['Data'] == '08-Jul-17']
pri = df.loc[df['Data'] == '01-Oct-17']

df = pd.concat([ver, out, inv, pri])

df.max()
df.min()
df.mean()

verS, outS, invS, priS = ver['sal'], out['sal'], inv['sal'], pri['sal']

verS.mean()
verS.max()
verS.min()
verS.std()

outS.mean()
outS.max()
outS.min()
outS.std()

invS.mean()
invS.max()
invS.min()
invS.std()

priS.mean()
priS.max()
priS.min()
priS.std()

ver_canal = ver[ver['sal'].isin(['st1', 'st7', 'st11'])]
ver_rio = ver[ver['sal'].isin(['st4', 'st5', 'st6'])]
ver_banco = ver[ver['sal'].isin(['st13','st16', 'st15', 'st17'])]

out_canal = out[out['sal'].isin(['st1', 'st2', 'st3' 'st7', 'st11', 'st14'])]
out_rio = out[out['sal'].isin(['st4', 'st5', 'st6'])]
out_banco = out[out['sal'].isin(['st13','st16', 'st15', 'st17'])]

inv_canal = inv[inv['sal'].isin(['st1', 'st2', 'st3','st7', 'st11' 'st14'])]
inv_rio = inv[inv['sal'].isin(['st4','st5', 'st6'])]
inv_banco = inv[inv['sal'].isin(['st13', 'st15', 'st17', 'st16'])]

pri_canal = pri[pri['sal'].isin(['st1', 'st2','st7', 'st11', 'st14'])]
pri_rio = pri[pri['sal'].isin(['st4','st5', 'st6'])]
pri_banco = pri[pri['sal'].isin(['st15', 'st16'])]

stats.kruskal(ver, inv)
stats.kruskal(inv, pri)
stats.kruskal(pri, ver)
stats.kruskal(verS, invS, priS)

stats.kruskal(pri_canal, pri_rio)
stats.kruskal(pri_rio, pri_banco)
stats.kruskal(pri_banco, pri_canal)
stats.kruskal(pri_canal, pri_rio, pri_banco)

stats.kruskal(ver_canal, ver_rio)
stats.kruskal(ver_rio, ver_banco)
stats.kruskal(ver_banco, ver_canal)
stats.kruskal(ver_canal, ver_rio, ver_banco)

stats.kruskal(inv_canal, inv_rio)
stats.kruskal(inv_rio, inv_banco)
stats.kruskal(inv_banco, inv_canal)
stats.kruskal(inv_canal, inv_rio, inv_banco)
