import numpy as np
import seaborn as sns
from os import path
from collections import OrderedDict
from matplotlib import pyplot as plt


class Saida:
    """docstring for Saida."""

    def __init__(self, cnv=None):
        super(Saida, self).__init__()
        self.cnv = cnv
        self.stations = OrderedDict()
        self.hd1 = []
        self.hd2 = []
        self.variables = []
        self.datapoints = []
        self.coordenadas = None
        self.df = None
        self.upcast = None
        if cnv:
            self.load(cnv)

    def load(self, cnv=None):

        """
        This function opens our .cnv file and reads it. It then creates a list
        with five elements: two lists containing the file headers (that start with
        * and with #), a list with variables, and a list of lists with the data itself.

        Run like the following:
        hd1, hd2, variables, datapoints = load('file')
        """

        if not path.isfile(cnv):
            raise ("Please provide a valid .cnv SeaBird MicroCat file.")
        else:
            self.cnv = cnv

        with open(self.cnv, encoding="iso-8859-1") as f:
            r = f.readlines()

        for line in r:
            if not line:
                pass
            elif line.startswith("*"):
                self.hd1.append(line.strip())
            elif line.startswith("#"):
                self.hd2.append(line.strip())
                if line.startswith("# name"):
                    line = line.split()
                    self.variables.append(line[4][:-1])
            else:
                float_list = []
                line = line.split()
                for item in line:
                    float_list.append(float(item))
                self.datapoints.append(float_list)

        self.datapoints = filter(None, self.datapoints)
        self.df = pd.DataFrame(self.datapoints, columns=self.variables)

    def get_upcast(self):
        self.upcast = self.df[self.df["c0S/m"] > 0.01]

    def split_stations(self):
        ix_ = 0
        values = pd.DataFrame()
        for ix, row in self.df.iterrows():
            if ix_ < len(self.coordenadas):
                if row["c0S/m"] >= 0.1:
                    station, lat, lon = (
                        self.coordenadas.Ponto.iloc[ix_],
                        self.coordenadas.Lat.iloc[ix_],
                        self.coordenadas.Lon.iloc[ix_],
                    )
                    row["name"] = station
                    row["lat"] = lat
                    row["lon"] = lon
                    values = values.append(row)
                elif row["c0S/m"] < 0.1:
                    if len(values) < 4:
                        values = pd.DataFrame()
                    elif len(values) >= 4:
                        print(f"Load station {self.coordenadas.Ponto.iloc[ix_]}.")
                        self.stations[self.coordenadas.Ponto.iloc[ix_]] = values
                        ix_ += 1
                        values = pd.DataFrame()


# Carregando dados
verao = Saida("data/ctd/stations_25-01-2017_processed.cnv")
outono = Saida("data/ctd/stations_27-05-2017_processed.cnv")
inverno = Saida("data/ctd/stations_08-07-2017_processed.cnv")
primavera = Saida("data/ctd/stations_01-10-2017_processed.cnv")
cc = pd.read_csv("data/csv/coordenadas_mare.csv", sep="\t")

# Carregando coordenadas
verao.coordenadas = cc[cc.Data.str.contains("25-Jan")]
outono.coordenadas = cc[cc.Data.str.contains("27-May")]
inverno.coordenadas = cc[cc.Data.str.contains("08-Jul")]
primavera.coordenadas = cc[cc.Data.str.contains("01-Oct")]

# Separando estações
for season in (verao, outono, inverno, primavera):
    season.get_upcast()
    season.split_stations()


# Limpando dados de clorofila
cc["CC"] = cc.CC.apply(lambda x: np.nan if x < 0 else x)
cc = cc[cc["CC"].notnull()]
cc["Estrat Temp"] = abs(cc["Surf Temp"] - cc["Bot Temp"])
cc["Estrat Sal"] = abs(cc["Surf Sal"] - cc["Bot Sal"])
cc["Secchi"] = pd.to_numeric(cc["Secchi"])

sns.lmplot("Surf Temp", "CC", data=cc)
sns.lmplot("Bot Temp", "CC", data=cc)
sns.lmplot("Estrat Temp", "CC", data=cc)
sns.lmplot("Surf Sal", "CC", data=cc)
sns.lmplot("Bot Sal", "CC", data=cc)
sns.lmplot("Estrat Sal", "CC", data=cc)
sns.distplot(cc["Estrat Sal"])

df = []
for season, season_name in zip(
    [verao, outono, inverno, primavera], ["verao", "outono", "inverno", "primavera"]
):
    for station, df_ in season.stations.items():
        df_["season"] = season_name
        df.append(df_)

df = pd.concat(df)


def get_zona(st):
    zonas = {
        "Canal": ("st1", "st2", "st3", "st7", "st11", "st14"),
        "Rio Tubarão": ("st4", "st5", "st6"),
        "Meio": ("st8", "st9", "st10", "st12", "st13", "st15", "st16", "st17"),
        "Ponte": ("st18", "st19", "st20"),
    }
    for k, v in zonas.items():
        if st in v:
            return k


df["zona"] = df.name.apply(lambda s: get_zona(s))

df.to_csv("data/csv/todas.csv", sep="\t", index=False)


# cc.to_csv("data/csv/coordenadas_processadas.csv", sep="\t", index=False)
