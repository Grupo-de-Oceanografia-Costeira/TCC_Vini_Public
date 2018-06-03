import pandas as pd
import matplotlib.pyplot as plt

from functions import *

# Load() function
hd1, hd2, variables, datapoints, df = load('sampling/cnv/stations_27-01-2017_processed.cnv')

# Defining 'stations', which will be arg2 for split_stations()
st_csv = pd.read_csv('sampling/27-01-17/coordenadas_2701.csv', sep = ';')
stations = list(st_csv['Ponto'])

# era para ter 26 estações, não sei quais são as outras 13 então botei isso
stations.extend(['o1','o2','o3','o4','o5','o6','o7','o8','o9','o10','o11','o12','o13'])

# split_stations() function
d = split_stations(datapoints, stations, variables)

for st in d:
    d[st] = remove_upcast(d[st])

locals().update(d)

plot(st2)
plot(st5c)
plot(st5b)
plot(st5a)
plot(st4)
plot(st3)
plot(st6)
plot(st7)
plot(st8)
plot(st9)
plot(st13)
plot(st12)
plot(st11)
plot(st10)
plot(st14)
plot(st17)
plot(st20)
plot(st19)
plot(st18)
plot(st21)
plot(st22)
plot(st23)
plot(st24)
plot(st25)
plot(st16)
plot(st15)

plot(st2, '.')
plot(st5c, '.')
plot(st5b, '.')
plot(st5a, '.')
plot(st4, '.')
plot(st3, '.')
plot(st6, '.')
plot(st7, '.')
plot(st8, '.')
plot(st9, '.')
plot(st13, '.')
plot(st12, '.')
plot(st11, '.')
plot(st10, '.')
plot(st14, '.')
plot(st17, '.')
plot(st20, '.')
plot(st19, '.')
plot(st18, '.')
plot(st21, '.')
plot(st22, '.')
plot(st23, '.')
plot(st24, '.')
plot(st25, '.')
plot(st16, '.')
plot(st15, '.')
