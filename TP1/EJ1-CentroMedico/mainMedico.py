import json,os
from clases import *
from clasesDB import *

os.system("cls")

DB_pacientes=ListaPacientes_DB()
DB_medicos=ListaMedicos_DB()

DB_medicos.view_list_turnos(input("Ingrese su DNI:"))

