import pandas
import time
from IPython import display
import matplotlib.pyplot as plt

class RegistrodeTiempos:

    def __init__(self,nombre_funcionalidad):
        self.nombre_estructura = ""
        self.nombre_funcionalidad = nombre_funcionalidad
        self.n_datos = 0

        self.tiempo_inicio = 0
        self.tiempo_fin = 0

        try:
            self.datos = pandas.read_csv("asintotico/{}.csv".format(self.nombre_funcionalidad),index_col="Numero de datos")
        except:
            self.datos = pandas.DataFrame(columns=["Array","LLT","DLL","CDLL","ColaArray","ColaLLT","ColaDLL","ColaCDLL"],
            index=[10**4,10**5,10**6,10**7])
            self.datos.index.name = "Numero de datos"

    def iniciar_conteo(self,n,nombre_estructura):
        self.tiempo_inicio = time.time()
        self.nombre_estructura = nombre_estructura
        self.n_datos = n

    def finalizar_conteo(self):
        self.tiempo_fin = time.time()
        self.datos[self.nombre_estructura][self.n_datos] = self.tiempo_fin-self.tiempo_inicio
        self.datos.to_csv("asintotico/{}.csv".format(self.nombre_funcionalidad))

    def retornar_grafica(self,estructuras_de_datos):
        self.datos[estructuras_de_datos].plot()
        plt.title("{}".format(self.nombre_funcionalidad))
        plt.ylabel("Tiempo (segundos)")
        plt.savefig("asintotico/{}.png".format(self.nombre_funcionalidad))

