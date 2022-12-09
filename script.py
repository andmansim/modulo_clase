from saludos import *  #Con esto ocupamos menos espacio en la memoria
from test.hola.saludos import Saludo
from test.adios.despedidas import Despedida

s = Saludo('A')
s.saludar()

d = Despedida('Adios')
d.despedida()
