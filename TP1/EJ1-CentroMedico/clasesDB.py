from clases import *

class ListaPacientes_DB: #(DB)
    def __init__(self):
        self._DB=[]

    #Metodos Privados
    #Por cada operacion que quiera realizar realizo una lectura para tenerla siempre actualizada
    def _get_DB(self):
        with open("ListaPacientes.json", "r") as archivo:
            self._DB = json.load(archivo)
           # print(self.DB)

   
    def _get_pos_paciente(self,dni):
        dni=int(dni)
        self._get_DB()
        #print(self.DB)
        for pos,paciente in enumerate(self._DB):
           if paciente["_dni"]==dni: return pos 
        return -1
    
    def _get_paciente(self,dni):
        self._get_DB
        pos=self._get_pos_paciente(dni)
        if(pos!=-1): return self._DB[pos]
        else: return -1


        
    def _get_historia_clinica(self,dni):
        self._get_DB()
        pos = self._get_pos_paciente(dni)
        if pos!=-1:
            return(self._DB[pos]["_list_historia_clinica"])


    #GETTERs / "ADDERs - PUBLICOS"
    def add_paciente(self,paciente):
        self._get_DB()
        self._DB.append(paciente.__dict__)
        with open("ListaPacientes.json", "w") as archivo:
            json.dump(self._DB,archivo,indent=3)
        

    def add_historia_clinica(self,dni,historia_clinica):
        pos=self._get_pos_paciente(dni)
        if pos!=-1: 
            self._get_DB()
            self._DB[pos]["_list_historia_clinica"].append(historia_clinica.__dict__)
            with open("ListaPacientes.json", "w") as archivo:
                 json.dump(self._DB,archivo,indent=3)

    
    def view_historia_clinica(self,dni):
        h_c=self._get_historia_clinica(dni)

        #print("\n\n Paciente : " + self.nombre)
        print("\n Historia Clinica: ")
        
        if(h_c!=[]):
            for i,consulta in enumerate( h_c):
                print("\n."+ str(i+1)+ ": "+ str(consulta["_fecha"]) + " Motivo : " +consulta["_sintomas"] + " \n Diagnóstico: " + consulta["_diagnostico"] + " \n\n")    
        else: print("No presenta Historia Clinica")


    def get_OS(self,dni):
        self._get_DB
        paciente=self._get_paciente(dni)
        return(paciente['_obra_social'])



class ListaMedicos_DB: #(DB)
    def __init__(self):
        self._DB=[]


    def _get_DB(self):
        with open("ListaMedicos.json", "r") as archivo:
            self._DB = json.load(archivo)

    def _get_pos_medico(self,dni):
        dni=int(dni)
        self._get_DB()
        for pos,medico in enumerate(self._DB):
           if medico["_dni"]==dni: return(pos)
           
        return -1
        
    def add_medico(self,medico):
        self._get_DB()
        self._DB.append(medico.__json__())
        with open("ListaMedicos.json", "w") as archivo:
            json.dump(self._DB,archivo,indent=3)
    
    def add_turno(self,turno,dni_medico):
        dni_medico=int(dni_medico)
        self._get_DB()
        pos=self._get_pos_medico(dni_medico)
        self._DB[pos]["_lista_turnos"].append(turno.__json__())
        with open("ListaMedicos.json", "w") as archivo:
            json.dump(self._DB,archivo,indent=3)

    def view_list_full(self):
        self._get_DB()
        for medico in self._DB:
            print("\n\n______________________________________________________")
            print(f" {medico['_nombre']} - {medico['_especialidad']}      Dni:{medico['_dni']} \n")
            if medico['_lista_turnos']!=[]:
                for turno in medico['_lista_turnos']:
                    print(f" Turno {turno['_turno']} : {turno['_paciente']}")
            else: print(" No hay turnos Registrados")


    def view_list_turnos(self,dni_medico):
        self._get_DB
        pos=self._get_pos_medico(dni_medico)
        medico=self._DB[pos]
        print(f"\n {medico['_nombre']}\n")
        if medico['_lista_turnos']!=[]:
            for turno in medico['_lista_turnos']:
                print(f" Turno {turno['_turno']} : {turno['_paciente']}")
        else: print(" No hay turnos Registrados")
        print("\n\n")

    def get_precio(self,dni):
        self._get_DB
        pos=self._get_pos_medico(dni)
        return(self._DB[pos]['_precio_consulta'])





    
