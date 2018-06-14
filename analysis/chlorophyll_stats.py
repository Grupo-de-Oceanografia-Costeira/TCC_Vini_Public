'''
'''

import pandas as pd
from scipy import stats

df = pd.read_csv('data/csv/coordenadas.csv', delimiter = ';')

cc = df['CC']
data = df['Data']
stations = df['Ponto']
df = pd.DataFrame([cc, data, stations])
df = df.transpose()

ver = df.loc[df['Data'] == '25-Jan-17']
inv = df.loc[df['Data'] == '08-Jul-17']
pri = df.loc[df['Data'] == '01-Oct-17']

df = pd.concat([ver, inv, pri])

df.max()
df.min()
df.mean()

verC, invC, priC = ver['CC'], inv['CC'], pri['CC']

verC.mean()
verC.max()
verC.min()
verC.std()

invC.mean()
invC.max()
invC.min()
invC.std()

priC.mean()
priC.max()
priC.min()
priC.std()

ver_canal = ver[ver['Ponto'].isin(['st7', 'st11', 'st14'])]
ver_rio = ver[ver['Ponto'].isin(['st5', 'st6'])]
ver_banco = ver[ver['Ponto'].isin(['st13', 'st15', 'st17'])]

inv_canal = inv[inv['Ponto'].isin(['st1', 'st2', 'st3', 'st14'])]
inv_rio = inv[inv['Ponto'].isin(['st5', 'st6'])]
inv_banco = inv[inv['Ponto'].isin(['st13', 'st17', 'st16'])]

pri_canal = pri[pri['Ponto'].isin(['st1', 'st2','st7', 'st14'])]
pri_rio = pri[pri['Ponto'].isin(['st4','st5'])]
pri_banco = pri[pri['Ponto'].isin(['st15', 'st16'])]

def kruskal2(x, y):
    x = [i for i in x['CC'] if str(i) != 'nan']
    y = [i for i in y['CC'] if str(i) != 'nan']
    return stats.kruskal(x, y)

def kruskal3(x, y, z):
    x = [i for i in x['CC'] if str(i) != 'nan']
    y = [i for i in y['CC'] if str(i) != 'nan']
    z = [i for i in z['CC'] if str(i) != 'nan']
    return stats.kruskal(x, y, z)

kruskal2(ver, inv)
kruskal2(inv, pri)
kruskal2(pri, ver)
kruskal3(ver, inv, pri)

kruskal2(pri_canal, pri_rio)
kruskal2(pri_rio, pri_banco)
kruskal2(pri_banco, pri_canal)
kruskal3(pri_canal, pri_rio, pri_banco)

kruskal2(ver_canal, ver_rio)
kruskal2(ver_rio, ver_banco)
kruskal2(ver_banco, ver_canal)
kruskal3(ver_canal, ver_rio, ver_banco)

kruskal2(inv_canal, inv_rio)
kruskal2(inv_rio, inv_banco)
kruskal2(inv_banco, inv_canal)
kruskal3(inv_canal, inv_rio, inv_banco)
