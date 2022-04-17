
from Estudiante import *

class AlmacenamientoEstudiantes:

    listaEstudiantes=[]
    listaGeneralEstudiantes=[]

    listaUsuarios=[]
    listaGeneralUsuarios=[]

    
    # Este metodo permitirá registrar estudiantes
    # en la lista de estudiantes y confirmar el registro
    def registrarEstudiante(self,estudiante):
        self.listaEstudiantes.append(estudiante)
        lista=[]
        lista.append(estudiante.documento)
        lista.append(estudiante.nombre)
        lista.append(estudiante.edad)
        lista.append(estudiante.telefono)
        lista.append(estudiante.talla)
        lista.append(estudiante.peso)
        lista.append(round(estudiante.imc,2))
        lista.append(estudiante.resultado)
        self.listaGeneralEstudiantes.append(lista)

        print(f"Estudiante {estudiante.nombre} registrado con exito!")

    def eliminarEstudiante(self,documento):
        print(documento)
        estudiante=self.consultarEstudiantePorDocumento(documento)
        if(estudiante!=None):
            nombre=estudiante.nombre
            for i in range(len(self.listaGeneralEstudiantes)):
                lista=self.listaGeneralEstudiantes[i]
                print("-->",lista)
                if(estudiante.documento==lista[0]):
                    print("Elimina")
                    self.listaGeneralEstudiantes.remove(lista)
                    self.listaEstudiantes.remove(estudiante)
                    break
        
        return f"El estudiante {nombre} Se ha eliminado con exito!"

    def actualizarEstudiante(self,miEstudiante):
        estudiante=self.consultarEstudiantePorDocumento(miEstudiante.documento)
        mensaje=""
        if(estudiante!=None):
            estudiante.nombre=miEstudiante.nombre
            estudiante.edad=miEstudiante.edad
            estudiante.telefono=miEstudiante.telefono
            estudiante.talla=miEstudiante.talla
            estudiante.peso=miEstudiante.peso
            estudiante.imc=miEstudiante.imc
            estudiante.resultado=miEstudiante.resultado
            self.actualizarListaGeneral(estudiante)
            mensaje="Se ha actualizado el estudiante"
        else:
            mensaje="El estudiante no se pudo actualizar"
        return mensaje

    def actualizarListaGeneral(self,estudiante):
        for i in range(len(self.listaGeneralEstudiantes)):
            lista=self.listaGeneralEstudiantes[i]
            print("-->",lista)
            if(estudiante.documento==lista[0]):
                print("Actualiza")
                lista[1]=estudiante.nombre
                lista[2]=estudiante.edad
                lista[3]=estudiante.telefono
                lista[4]=estudiante.talla
                lista[5]=estudiante.peso
                lista[6]=round(estudiante.imc,2)
                lista[7]=estudiante.resultado
                break


    def obtenerListaEstudiantes(self):
        print(self.listaGeneralEstudiantes)
        return self.listaGeneralEstudiantes

    def consultarListaEstudiantes(self):
        if(self.validaTamanioLista()==True):
            for i in range(len(self.listaEstudiantes)):
                estudiante=self.listaEstudiantes[i]
                estudiante.imprimirDatos()
        
        return self.listaEstudiantes


    def consultarEstudiantePorDocumento(self,documento):
        estudiante=None #Se inicializa en none el estudiante
        if(self.validaTamanioLista()==True):
            for est in self.listaEstudiantes:
                if(est.documento==documento):
                    estudiante=est # se asigna el elemento encontrado al objeto estudiante
        
        return estudiante


    def consultarResultados(self,resultado):
        cant=0
        if(self.validaTamanioLista()==True):
            for est in self.listaEstudiantes:
                if(est.resultado==resultado):
                    cant+=1
        
        return cant
        

    def obtenerCantidadEstudiantes(self):
        return len(self.listaEstudiantes)

    
    def validaTamanioLista(self):
        if(len(self.listaEstudiantes)>0):
            return True
        else:
            print("\n<<<< No han registrado estudiantes >>>")
            return False




