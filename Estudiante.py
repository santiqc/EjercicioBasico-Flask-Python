class Estudiante:

    def __init__(self,documento=None,nombre=None,edad=None,
                    telefono=None,talla=None,peso=None,imc=None,res=None):
        self.documento=documento
        self.nombre=nombre
        self.edad=edad
        self.telefono=telefono
        self.talla=talla
        self.peso=peso
        self.imc=imc
        self.resultado=res

    def imprimirDatos(self):
        datos="\n<<<<<<<<<<<<< DATOS ESTUDIANTE >>>>>>>>>>>>>>>\n"
        datos+=f"Documento: {self.documento} , Nombre: {self.nombre}\n"
        datos+=f"Edad: {self.edad} años , Telefono: {self.telefono}\n"
        datos+=f"Talla: {self.talla} cm , Peso: {self.peso} kg\n"
        datos+=f"IMC: {self.imc} , Resultado: {self.resultado}\n"

        print(datos)


