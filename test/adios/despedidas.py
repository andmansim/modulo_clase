def despedida():
    print('Adios')
    print('Hasta luego')
    print('Hasta nunca')

class Despedida():
    def __init__(self, nombre):
        self.nombre = nombre
    def despedida(self):
        print('Adios' + self.nombre)
        print('Hasta luego' + self.nombre)
        print('Hasta nunca' + self.nombre)