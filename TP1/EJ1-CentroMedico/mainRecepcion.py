import json,os
from clases import *
from clasesDB import *

os.system("cls")

DB_pacientes=ListaPacientes_DB()
DB_medicos=ListaMedicos_DB()

def crear_paciente(dni):
    os.system("cls")
    print("\n REGISTRAR NUEVO PACIENTE AL SISTEMA")
    paciente=Paciente(input("\n Nombre: "),input("\n Sexo: "),input("\n Edad: "),dni,input("\n Obra Social: "))
    os.system("cls")
    return(paciente)

def crear_historia_clinica(paciente):
    os.system("cls")
    print(paciente)
    #print(f"{paciente['_nombre']} | Obra Social: {paciente['_obra_social']} | DNI: {paciente['_dni']} | Edad: {paciente['_edad']} ")
    h_c=HistoriaClinica("01/06/23",input("Motivo de la visita: "),"")
    return(h_c)

def asignar_turno(dni_paciente):
    os.system("cls")
    print("\n AGENDAR TURNO: \n")
    DB_medicos.view_list_full()
    turno=Turno(input("\nHorario Deseado: ",),dni_paciente) 
    dni_medico=input("Medico Seleccionado (DNI):")
    DB_medicos.add_turno(turno,dni_medico)
    return(dni_medico)

def pago(dni_paciente,dni_medico):
    obra_social=DB_pacientes.get_OS(dni_paciente)
    if  obra_social!= "":
        print(f"\n Posee Obra Social {obra_social} no debe realizar ningun pago.")
    else: print(f" No posee Obra Social. Debe Pagar $ {DB_medicos.get_precio(dni_medico)}")

    



print("\nINGRESO PACIENTES")
dni_paciente=input("\n Dni Paciente: ")

#1 Evaluo si Existe en el sistema. Caso contrario lo Registro
paciente=DB_pacientes._get_paciente(dni_paciente)
if(paciente==-1):  
    paciente=crear_paciente(dni_paciente)
    DB_pacientes.add_paciente(paciente)
#2 Agrego la visita a su historia Clinica
h_c=crear_historia_clinica(paciente)
DB_pacientes.add_historia_clinica(dni_paciente,h_c)
#3 Asigno el turno e informo de Pago
dni_medico=asignar_turno(dni_paciente)
pago(dni_paciente,dni_medico)






