import json
from clases import *
from clasesDB import *


#Ejemplo

try:
    with open("ListaPacientes.json", "r") as archivo:
        datos = json.load(archivo)
except FileNotFoundError:
    datos = []


paciente1 = Paciente("Jose","masc",34,10000,"Red de Seguros")
paciente2 = Paciente("Pepe","masc",27,10001,"Asunt")

datos.extend([(paciente1.__dict__),paciente2.__dict__])
print(datos)

''' "with" Explicacion
Cuando se utiliza el bloque with, 
se asegura que el método __enter__() del objeto <context> se 
llame al entrar en el bloque y que el método __exit__() se llame al salir del bloque, 
independientemente de si se produce una excepción o no. Estos métodos permiten que el 
objeto realice tareas de inicialización y limpieza de forma automática.
'''

with open("ListaPacientes.json", "w") as archivo:
    json.dump(datos,archivo,indent=3)

