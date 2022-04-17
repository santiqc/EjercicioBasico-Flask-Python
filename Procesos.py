from Estudiante import *
from Usuario import *
from AlmacenamientoEstudiantes import *
from AlmacenamientoUsuarios import *

class Procesos:

    usuarioGlobal=None
    miAlmacenamiento=AlmacenamientoEstudiantes()
    miAlmacenamientoUsuarios=AlmacenamientoUsuarios()

# Lógica Gestión de Usuarios

    def llenarListaUsuarios(self):
        miUsuarioAdmin = Usuario("admin","admin","NA","admin@gmail.com","admin",1)
        miUsuario1 = Usuario("1094","Cristian Henao","3113458921","cdhenao9@misena.edu.co","1094",1)
        miUsuario2 = Usuario("111","Maria","344563","maria@gmail.com","111",1)
        miUsuario3 = Usuario("222","Pepe","43214","pepe@gmail.com","222",2)
        miUsuario4 = Usuario("333","Juan Pablo","654356","juan@gmail.com","333",2)
        miUsuario5 = Usuario("444","Angela Zapata","876543","angela@gmail.com","444",2)
    
        print()
        self.miAlmacenamientoUsuarios.registrarUsuario(miUsuarioAdmin)
        self.miAlmacenamientoUsuarios.registrarUsuario(miUsuario1)
        self.miAlmacenamientoUsuarios.registrarUsuario(miUsuario2)
        self.miAlmacenamientoUsuarios.registrarUsuario(miUsuario3)
        self.miAlmacenamientoUsuarios.registrarUsuario(miUsuario4)
        self.miAlmacenamientoUsuarios.registrarUsuario(miUsuario5)

    def registrarUsuarios(self,miUsuario):
        print("Usuario a registrar",miUsuario)
        return self.miAlmacenamientoUsuarios.registrarUsuario(miUsuario)

    def actualizarUsuario(self,miUsuario):
        return self.miAlmacenamientoUsuarios.actualizarUsuario(miUsuario)

    def eliminarUsuario(self,documento):
        return self.miAlmacenamientoUsuarios.eliminarUsuario(documento)


    def consultarUsuario(self,documento):
        usuario=self.miAlmacenamientoUsuarios.consultarUsuarioPorDocumento(documento)

        if(usuario!=None):
            print(usuario)
        else:
            print(f"\nNo existe ningún estudiante con el documento {documento}")
            
        return usuario

    def obtenerListaUsuarios(self):
        lista=self.miAlmacenamientoUsuarios.obtenerListaUsuarios()  
        return lista 
    
    def consultarListaUsuarios(self):
        print("\n<<<<<<<<<<<<<<<<<- LISTA DE ESTUDIANTES ->>>>>>>>>>>>>>>>>>>>")
        self.miAlmacenamientoUsuarios.consultarListaUsuarios()  
        print("\n*************************************************************\n")    

# Lógica Gestión de Estudiantes

    def llenarListaEstudiantes(self):
        miEstudiante1 = Estudiante("111","Juan",21,"344563",1.75,76,self.calcularIMC(1.75,76),self.calcularResultadoIMC(self.calcularIMC(1.75,76)))
        miEstudiante2 = Estudiante("222","Pedro",20,"43214",1.65,86,self.calcularIMC(1.65,86),self.calcularResultadoIMC(self.calcularIMC(1.65,86)))
        miEstudiante3 = Estudiante("333","Maria",23,"654356",1.70,70,self.calcularIMC(1.70,70),self.calcularResultadoIMC(self.calcularIMC(1.70,70)))
        miEstudiante4 = Estudiante("444","Carlos",21,"876543",1.80,86,self.calcularIMC(1.80,86),self.calcularResultadoIMC(self.calcularIMC(1.80,86)))
        
        print()
        self.miAlmacenamiento.registrarEstudiante(miEstudiante1)
        self.miAlmacenamiento.registrarEstudiante(miEstudiante2)
        self.miAlmacenamiento.registrarEstudiante(miEstudiante3)
        self.miAlmacenamiento.registrarEstudiante(miEstudiante4)

    
    def registrarEstudiante(self,miEstudiante):
        print(miEstudiante)
        '''
        miEstudiante = Estudiante()
        miEstudiante.documento=input("\nIngrese el documento del estudiante: ")
        miEstudiante.nombre=input("Ingrese el nombre del estudiante: ")
        miEstudiante.edad=input("Ingrese la edad del estudiante: ")
        miEstudiante.telefono=input("Ingrese el telefono del estudiante: ")
        miEstudiante.talla=float(input("Ingrese la talla: "))
        miEstudiante.peso=float(input("Ingrese el peso: "))
        '''
        imc=self.calcularIMC(miEstudiante.talla, miEstudiante.peso)
        miEstudiante.imc=imc
        miEstudiante.resultado=self.calcularResultadoIMC(imc)
        print()
        self.miAlmacenamiento.registrarEstudiante(miEstudiante)

    def actualizarEstudiante(self,miEstudiante):
        imc=self.calcularIMC(miEstudiante.talla, miEstudiante.peso)
        miEstudiante.imc=imc
        miEstudiante.resultado=self.calcularResultadoIMC(imc)
        return self.miAlmacenamiento.actualizarEstudiante(miEstudiante)

    def eliminarEstudiante(self,documento):
        return self.miAlmacenamiento.eliminarEstudiante(documento)


    def consultarEstudiante(self,documento):
        #documento=input("\nIngrese el documento del estudiante a consultar: ")
        estudiante=self.miAlmacenamiento.consultarEstudiantePorDocumento(documento)

        if(estudiante!=None):
            print(estudiante.imprimirDatos())
        else:
            print(f"\nNo existe ningún estudiante con el documento {documento}")
            
        return estudiante

    def obtenerListaEstudiantes(self):
        lista=self.miAlmacenamiento.obtenerListaEstudiantes()  
        return lista 
    
    def consultarListaEstudiantes(self):
        print("\n<<<<<<<<<<<<<<<<<- LISTA DE ESTUDIANTES ->>>>>>>>>>>>>>>>>>>>")
        self.miAlmacenamiento.consultarListaEstudiantes()  
        print("\n*************************************************************\n")    

    def consultarResultados(self):
        print()
        print("<<<<<<<<<< RESULTADOS >>>>>>>>>>>>>")
        print("Estudiantes Registrados:",self.miAlmacenamiento.obtenerCantidadEstudiantes())
        print("Anorexia: ",self.miAlmacenamiento.consultarResultados("Anorexia")) 
        print("Delgadez: ",self.miAlmacenamiento.consultarResultados("Delgadez")) 
        print("Normalidad: ",self.miAlmacenamiento.consultarResultados("Normalidad")) 
        print("Obesidad (Grado 1): ",self.miAlmacenamiento.consultarResultados("Obesidad (Grado 1)")) 
        print("Obesidad (Grado 2): ",self.miAlmacenamiento.consultarResultados("Obesidad (Grado 2)")) 
        print("Obesidad (Grado 3): ",self.miAlmacenamiento.consultarResultados("Obesidad (Grado 3)")) 
        print("Obesidad Morbida: ",self.miAlmacenamiento.consultarResultados("Obesidad Morbida"))  

    def calcularIMC(self,talla,peso):
        imc=peso/(talla*talla)  
        return imc

    def calcularResultadoIMC(self, imc):
        resultado=""
        if(imc<18):
            resultado="Anorexia"
        elif(imc>=18 and imc<20):
            resultado="Delgadez"
        elif(imc>=20 and imc<27):
            resultado="Normalidad"
        elif(imc>=27 and imc<30):
            resultado="Obesidad (Grado 1)"
        elif(imc>=30 and imc<35):
            resultado="Obesidad (Grado 2)"
        elif(imc>=35 and imc<40):
            resultado="Obesidad (Grado 3)"
        elif(imc>=40):
            resultado="Obesidad Morbida"

        return resultado
