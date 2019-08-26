import seaborn as sns
from os import path
from collections import OrderedDict


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
            if row["c0S/m"] >= 0.1:
                row["name"] = verao.coordenadas.Ponto.iloc[ix_]
                row["lat"] = verao.coordenadas.Lat.iloc[ix_]
                row["lon"] = verao.coordenadas.Lon.iloc[ix_]
                values.append(row)
            elif row["c0S/m"] < 0.1:
                if len(values) < 4:
                    values = pd.DataFrame()
                elif len(values) >= 4:
                    self.stations[verao.coordenadas.Ponto.iloc[ix_]] = values
                    ix_ += 1


verao = Saida("data/ctd/stations_25-01-2017_processed.cnv")
coordenadas = pd.read_csv("data/csv/coordenadas.csv", sep=";")
verao.coordenadas = coordenadas[coordenadas.Data.str.contains("25")]
# verao.split_stations()
verao.get_upcast()
verao.upcast

sns.distplot(verao.upcast["c0S/m"])
sns.distplot(verao.upcast["t090"])
sns.distplot(verao.upcast["pr"])
sns.distplot(verao.upcast["sal00"])
