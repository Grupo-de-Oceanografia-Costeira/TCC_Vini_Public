import pandas as pd
import numpy as np
import collections
import os
import glob
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def load(cnv):

    '''
    This function opens our .cnv file and reads it. It then creates a list
    with five elements: two lists containing the file headers (that start with
    * and with #), a list with variables, a list with the data itself, and a
    pandas dataframe with the data.

    Run like the following:
    hd1, hd2, variables, datapoints, df = load('file')
    '''

    o = open(cnv)
    r = o.readlines()
    o.close()

    hd1, hd2, variables, datapoints = [], [], [], []

    for line in r:
        if not line:
            pass
        elif line.startswith('*'):
            hd1.append(line)
        elif line.startswith('#'):
            hd2.append(line)
            if line.startswith('# name'):
                line = line.split()
                variables.append(line[4])
        else:
            float_list = []
            line = line.split()
            for item in line:
                float_list.append(float(item))
            datapoints.append(float_list)

    datapoints = filter(None, datapoints)
    df = pd.DataFrame(datapoints, columns = variables)

    return hd1, hd2, variables, datapoints, df

def split_stations(arg1, arg2, arg3 = None, arg4 = None, arg5 = None):
    '''
    arg1 is a list of lists, each list being a row of data, like the
    'datapoints' variable generated in the load() function. arg2 is a list of
    strings with the station names IN THE ORDER THEY WERE SAMPLED. This can
    be loaded from a .csv file. arg3 is a list of the variables that will be
    the columns for the resulting dataframes. It should be generated with the
    load() function.
    '''
    d = collections.OrderedDict()

    for st in arg2:
        d[st] = []

    ix = 0
    st_values = []

    for line in arg1:
        if line[1] >= 0.1:
            line.append(arg2[ix]) # station names
            line.append(arg4[ix]) # station lat
            line.append(arg5[ix]) # station lon
            st_values.append(line)
        elif line[1] < 0.1:
            if len(st_values) < 4:
                st_values = []
            elif len(st_values) >= 4:
                for line in st_values:
                    d[arg2[ix]].append(line)
                st_values = []
                ix += 1
    arg3.append('STATION')
    arg3.append('LAT')
    arg3.append('LONG')

    for st in d:
        d[st] = pd.DataFrame(d[st], columns = arg3)

    return d

def remove_upcast(station):
    depth = station['depSM:']
    up = depth.idxmax() + 1 # we want the index, not the value
    station = station.loc[:up]
    return station


def plot(arg1, arg2=None):
    '''
    Easy temperature, salinity and density multiplot

    To-do:
    - xlim = span from 'hd2' variable
    '''

    fig,(ax1, ax2, ax3) = plt.subplots(1, 3, sharey = True)
    tem, dep, tim, sal, den = arg1['t090:'], arg1['depSM:'], arg1['timeJ:'], arg1['sal00:'], arg1['sigma-t00:']
    i1 = interp1d(tem, dep, kind='cubic')
    i2 = interp1d(sal, dep, kind='cubic')
    i3 = interp1d(den, dep, kind='cubic')

    ax1.plot(tem, dep, 'o', tem, i1(tem), '--', color = 'red')
    ax1.set_ylabel('Depth [m]')
    ax1.set_title('Temperature [deg C]')
    ax2.plot(sal, dep, 'o', sal, i2(sal), '--', color = 'blue')
    ax2.set_title('Salinity [PSU]')
    ax3.plot(den, dep, 'o', den, i3(den), '--', color = 'green')
    ax3.set_title('Density [kg/m^3]')

    plt.ylim((-0.5,8.0))
    plt.gca().invert_yaxis()
    title = str(arg1)

    if arg2 is None:
        plt.show()
    else:
        fname = arg2 + '/' + arg1['Station ID'][0] + '.png'
        plt.savefig(fname)
