from abc import ABC,abstractclassmethod
import json

class Consultorio():
    #@abstractclassmethod    #Abstraigo Constructor => Clase Abstracta ! Genera errores al generar un Json.
    def __init__(self,ubicacion,numero):
        self._ubicacion=ubicacion
        self._numero=numero
        
    def __json__(self):
        return{
            '_ubicacion':self._ubicacion,
            '_numero':self._numero
        }

class Turno:
    def __init__(self,turno,_dni_paciente):
        self._turno=turno
        self._dni_paciente=_dni_paciente

    def __json__(self):
        return{
            '_turno':self._turno,
            '_paciente':self._dni_paciente
        }
        



class Persona(ABC):
    #@abstractclassmethod   ! Genera errores al generar un Json.
    def __init__(self,nombre,sexo,edad,dni):
        
        self._nombre=nombre
        self._sexo=sexo
        self._edad=int(edad)
        self._dni=int(dni)
        
        
    
class Medico(Persona):
    def __init__(self,nombre,sexo,edad,dni,especialidad,precio_consulta,h,consultorio):
        super().__init__(nombre,sexo,edad,dni) #constructor por herencia

        self._especialidad=especialidad
        self._precio_consulta=precio_consulta

        self._horarios = {"Lunes":[h[0][0],h[0][1]],"Martes":[h[1][0],h[1][1]],"Miercoles":[h[2][0],h[2][1]],"Jueves":[h[3][0],h[3][1]],
                         "Viernes":[h[4][0],h[4][1]],"Sabado":[h[5][0],h[5][1]],"Domingo":[h[6][0],h[6][1]]}
        
        #Instancio en Constructor ya que se trata de una Asociacion de Composicion
        self._consultorio =Consultorio(consultorio[0],consultorio[1])
        self._lista_turnos=[]
  

    def __json__(self):
        return{
            '_nombre': self._nombre,
            '_sexo': self._sexo,
            '_edad': self._edad,
            '_dni': self._dni,
            '_especialidad': self._especialidad,
            '_precio_consulta': self._precio_consulta,
            '_horarios': self._horarios,
            '_consultorio':self._consultorio.__json__(),
            '_lista_turnos': self._lista_turnos
        }
    
    def set_horario(self,dia,pos,valor):  #Por ahora no se tendran en cuenta los min

        dia=dia.capitalize()
        validos=["Lunes","Martes","Miercoles","Jueves","Viernes"]

        if (dia in validos):
            print("Por favor ingrese un día válido")
            return
        

        self._horarios.dia[pos]=valor

    def ver_turnos(self):
        print(f'''TURNOS: \n
              ''')



class HistoriaClinica:
    def __init__(self,fecha,sintomas,diagnostico):
        self._fecha=fecha
        self._sintomas=sintomas
        self._diagnostico = diagnostico
    




class Paciente(Persona):
    def __init__(self,nombre,sexo,edad,dni,obra_social):
        super().__init__(nombre,sexo,edad,dni) #constructor por herencia
        self._obra_social=obra_social

        self._list_historia_clinica=[]

    def __str__(self):
        return f"{self._nombre}\t- {self._sexo}\t Edad: [{self._edad}]\t Dni: [{self._dni}]\t OS: [{self._obra_social}]"


    





   
        
 
       