from setuptools import setup

setup(
    name = 'paquete',
    version = '1.0',
    description = 'Paquete de prueba',
    author = 'Andrea',
    package =['paquete','paquete.hola','paquete.adios'], #otra opcion era poner __all__ en el init, ns que es
    scripts = ['']

)
#Se supone que tiene que crear una capeta dist, donde hay un archivo llamado paquete 
#Sacamos el archivo de la carpeta y lo instalameos en la terminal con pip install (nombre del archivo ), si lo queremos desinstalar es con uninstall
#Creo que es para crear nuestras propias librerías


