#1 Importo todo de mi UI.py
import sys
from Vista.UI_main import *
from Vista.UI_tabla import *
from PyQt5.QtWidgets import QDialog,QTableWidgetItem 


#2 Importo Modelo
from Modelo.GestorDB import *

class MiMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

    #Aqui Escribo mis funciones self.boton.clicked.conect(self.mifuncion)
        self.listar_button.clicked.connect(self.exec_listar)

    def exec_listar(self):
        lista_lotes= ListaLotes()
        lista_lotes.exec_()
        
class ListaLotes(QDialog):

    def __init__(self):
        super().__init__() #inicializo clase heredada
        self.form=Ui_FromTabla()   #creo Tabla
        self.form.setupUi(self)    #iniclizo la interdaz de tabla

        #CONFIGURANDO LA TABLA  
        self.DB=get_all_lotes()
        self.form.tablaLotes.setColumnCount(10)
        self.form.tablaLotes.setRowCount(len(self.DB))
        headers=['ID','m2','UBICACION','PRECIO ($)','ESTADO','DUEÑO','PAGADO','CUOTA','VENC PROX','VENCIDAS']
        self.form.tablaLotes.setHorizontalHeaderLabels(headers)
        
        #Parte 1 de tabla. Desde IDlote hasta Duenio
        P1=get_id_m2_ubic_precio_estado_duenio()

        for indexF,fila in enumerate(P1):
            for indexC,valor in enumerate(fila):
                self.form.tablaLotes.setItem(indexF,indexC,QTableWidgetItem(str(valor)))



        
        





if __name__ == "__main__":                  #evitar ejecuciones duplicadas
    app = QtWidgets.QApplication([])
    window = MiMainWindow()
    window.show()
    app.exec_()