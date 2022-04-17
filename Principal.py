from re import U
from flask import Flask, render_template, request
from Procesos import *

app = Flask(__name__)

titulos=("Documento","Nombre","Edad","Telefono","Talla","Peso","IMC","Resultado")
titulosTablaUsuarios=("Documento","Nombre","Telefono","Correo","Tipo")

misProcesos=Procesos()
misProcesos.llenarListaUsuarios()
misProcesos.llenarListaEstudiantes()

@app.route("/")
def index():
    return render_template('login.html')

@app.route("/pagina")
def pagina():
    return render_template('pagina.html')

@app.route("/inicio")
def inicio():
    return render_template('inicio.html',user=Procesos.usuarioGlobal)

@app.route("/registrar")
def registro():
    return render_template('registro.html',user=Procesos.usuarioGlobal)

@app.route("/form")
def form():
    return render_template('form.html')

@app.route("/consultar")
def consulta():
    informacion=misProcesos.obtenerListaUsuarios()
    return render_template('consulta.html',titulos_tabla=titulosTablaUsuarios,data=informacion,user=Procesos.usuarioGlobal)

@app.route("/gestion_estudiantes")
def gestion_estudiantes():
    informacion=misProcesos.obtenerListaEstudiantes()
    return render_template('gestion_estudiantes.html',titulos_tabla=titulos,data=informacion,user=Procesos.usuarioGlobal)

@app.route("/gestion_usuarios")
def gestion_usuario():
    return render_template('gestionar_usuarios.html',user=Procesos.usuarioGlobal)

@app.route("/valida_usuarios", methods=['GET', 'POST'])
def valida_usuarios():
    resultado=""
    if request.method == 'POST':

            usuario=None
            documento=request.form['documento']
            nombre=request.form['nombre']
            telefono=request.form['telefono']
            email=request.form['email']
            tipo=int(request.form['tipo'])

            if ('buscar' in request.form):
                usuario=misProcesos.consultarUsuario(documento)
                if(usuario==None):
                    resultado="El usuario no se encuentra registrado!"

            elif('registrar' in request.form):
                print("Registrar")
                usuario=misProcesos.consultarUsuario(documento)
                if usuario==None:
                    usuario=Usuario(documento,nombre,telefono,email,documento,tipo)
                    misProcesos.registrarUsuarios(usuario)
                    resultado=misProcesos.registrarUsuarios(usuario)
                else:
                    resultado=f"El documento ya se encuentra registrado y corresponde a {usuario.nombre}"
            elif('actualizar' in request.form):
                print("actualizar")
                usuario=Usuario(documento,nombre,telefono,email,documento,tipo)
                resultado=misProcesos.actualizarUsuario(usuario)
            elif('eliminar' in request.form):
                print("eliminar")
                usuario=None
                resultado=misProcesos.eliminarUsuario(documento)

            print("**********************")
            print("VALOR DE USUARIO",usuario)
            if(usuario!=None):
                datos={
                    "documento":usuario.documento,
                    "nombre":usuario.nombre,
                    "telefono":usuario.telefono,
                    "email":usuario.email,
                    "tipo":usuario.tipo,
                    "resultado":resultado
                    }
            else:
                datos={
                    "documento":"",
                    "nombre":"",
                    "edad":"",
                    "telefono":"",
                    "talla":"",
                    "peso":"",
                    "resultado":resultado
                    }

            print(datos)
    return render_template('gestionar_usuarios.html',usuario=datos,user=Procesos.usuarioGlobal)


@app.route('/inicio_sesion', methods=['POST'])
def inicio_sesion():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        Procesos.usuarioGlobal=misProcesos.consultarUsuario(usuario)
        print(f"usuario Ingresado:{usuario}, pass:{password}")
        print(f"usuario encontrado:{Procesos.usuarioGlobal}")
        if Procesos.usuarioGlobal!=None:
            if(usuario==Procesos.usuarioGlobal.documento and password==Procesos.usuarioGlobal.password):
                return render_template('inicio.html',user=Procesos.usuarioGlobal)

        return render_template('login.html',user=None)

@app.route("/registro_usuario", methods=['GET', 'POST'])
def registrarUsuario():
    resultado=None
    documento,nombre,telefono,email,tipo="","","","",""

    if request.method == 'POST':
        usuario=None
        documento=request.form['documento']
        nombre=request.form['nombre']
        telefono=request.form['telefono']
        email=request.form['email']
        tipo=int(request.form['tipo'])

        print("Registrar")
            
        usuario=misProcesos.consultarUsuario(documento)
        if usuario==None:
            usuario=Usuario(documento,nombre,telefono,email,documento,tipo)
            misProcesos.registrarUsuarios(usuario)
            resultado=misProcesos.registrarUsuarios(usuario)
        else:
            resultado=f"El documento ya se encuentra registrado y corresponde a {usuario.nombre}"       
      

        datos={
            "resultado":resultado
        }

    return render_template('registro.html',data=datos)


@app.route("/validacion", methods=['GET', 'POST'])
def validacion():
    informacion=misProcesos.obtenerListaEstudiantes()
    resultado=None
    documento,nombre,telefono,edad,talla,peso="","","","","",""
    if request.method == 'POST':

            estudiante=None
            documento=request.form['documento']
            nombre=request.form['nombre']
            edad=request.form['edad']
            telefono=request.form['telefono']
            talla=request.form['talla']
            peso=request.form['peso']

            if ('buscar' in request.form):
                estudiante=misProcesos.consultarEstudiante(documento)
                if(estudiante!=None):
                    resultado=f"IMC: {round(estudiante.imc,2)} con Resultado: {estudiante.resultado}"
                else:
                    resultado="La persona no se encuentra registrada"
            elif('registrar' in request.form):
                print("Registrar")
                estudiante=misProcesos.consultarEstudiante(documento)
                if estudiante==None:
                    estudiante=Estudiante(documento,nombre,int(edad),telefono,float(talla),float(peso))
                    misProcesos.registrarEstudiante(estudiante)
                    resultado="Registro Exitoso."
                else:
                    resultado=f"El documento ya se encuentra registrado y corresponde a {estudiante.nombre}"

                
            elif('actualizar' in request.form):
                print("actualizar")
                estudiante=Estudiante(documento,nombre,int(edad),telefono,float(talla),float(peso))
                resultado=misProcesos.actualizarEstudiante(estudiante)
            elif('eliminar' in request.form):
                print("eliminar")
                estudiante=None
                resultado=misProcesos.eliminarEstudiante(documento)

            print("**********************")
            print(estudiante)
            if(estudiante!=None):
                datos={
                    "documento":estudiante.documento,
                    "nombre":estudiante.nombre,
                    "edad":estudiante.edad,
                    "telefono":estudiante.telefono,
                    "talla":estudiante.talla,
                    "peso":estudiante.peso,
                    "resultado":resultado
                    }
            else:
                    datos={
                    "documento":"",
                    "nombre":"",
                    "edad":"",
                    "telefono":"",
                    "talla":"",
                    "peso":"",
                    "resultado":resultado
                    }

            print(datos)
        
    return render_template('gestion_estudiantes.html',titulos_tabla=titulos,data=informacion,estudiante=datos,user=Procesos.usuarioGlobal)




if (__name__ == '__main__'):
    app.run(debug=True,port=5000)




