import json
from clases import *
from clasesDB import *


#Ejemplo



try:
    with open("ListaMedicos.json", "r") as archivo:
        datos = json.load(archivo)
except FileNotFoundError:
    datos = []


horarios_m1=[[8,17],[8,17],[8,17],[8,17],[8,17],[8,12],[None,None]]
medico1=Medico("Juarez Emilio","masc",54,"10000","Pediatra",1500,horarios_m1,["SEDE CENTRAL | Corrientes 460",1])

horarios_m2=[[15,20]]*6 + [[None, None]]
medico2=Medico("Lobo Eugenio","masc",48,"10001","Cardiologo",1001,horarios_m2,["SEDE CENTRAL | Corrientes 460",2])

horarios_m3=[[10,18]]*6 + [[None, None]]
medico3=Medico("Novillo Jose","masc",43,"10002","Cirujano",1002,horarios_m3,["SEDE YERBA BUENA | Av Aconquija 941",3])




datos.extend([medico1.__json__(),medico2.__json__(),medico3.__json__()])
print(datos)



with open("ListaMedicos.json", "w") as archivo:
    json.dump(datos,archivo,indent=3)

