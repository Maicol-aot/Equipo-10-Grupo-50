import os
from flask import Flask, render_template, request, flash, redirect, url_for
from flask.json import jsonify
from db import get_db, close_db

app=Flask(__name__)
app.secret_key=os.urandom(24)

@app.route("/", methods=["GET"])
def inicio():
    return render_template('/index.html')

@app.route("/sign_up", methods=["GET", "POST"])
def signup():
    if request.method=="POST":
        nombre=request.form['nombre']
        apellido=request.form['apellido']
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']
        sexo=request.form['sexo']
        edad=request.form['edad']

        db=get_db()

        if len(password) < 8:
            print('no es valido')
            error="La contaseña debe contener minimo 8 caracteres"
            return(error)

        if db.execute(' SELECT id FROM usuarios WHERE username = ?', (username,)).fetchone()is not None: 
            error = " El nombre de usuario ya existe"
            return (error)

        if db.execute(' SELECT id FROM usuarios WHERE email = ?', (email,)).fetchone()is not None: 
            error = " El Correo ya existe".format( email )
            return (error)
        else:
            db.execute('INSERT INTO usuarios(nombre, apellido, username, email, password, sexo, edad) VALUES (?,?,?,?,?,?,?)', (nombre, apellido, username, email, password, sexo, edad))
            db.cursor()
            db.commit()
            return redirect("usuario", usr=username)
    else:
        return render_template('sign_up.html')
    

@app.route("/sign_in", methods=["GET", "POST"])
def login():
    return render_template('sign_in.html')

@app.route("/feed", methods=["GET"])
def feed():
    return render_template('/feed.html')

@app.route("/publicacion/<id_publicacion>", methods=["GET"])
def publicacion(id_publicacion):
    return render_template('/detalles-publicacion.html')

@app.route("/perfil_usuario/<usr>", methods=["GET", "POST"])
def perfil_usuario(usr):
    return render_template('/perfil_usuario.html')

@app.route("/administrador", methods=["GET", "POST"])
def administrador():
    return render_template('/administrador.html')

@app.route("/Enviar_Mensaje", methods=["GET", "POST"])
def mensajes():
    return render_template('/Enviar_Mensaje.html')

@app.route("/Eliminar_Usuario", methods=["GET", "POST"])
def eliminar_usuario():
    return render_template('/Eliminar_Usuario.html')

@app.route("/Eliminar_Publicacion", methods=["GET", "POST"])
def eliminar_publicacion():
    return render_template('/Eliminar_Publicacion.html')

@app.route("/Editar_Usuario", methods=["GET", "POST"])
def editar_usuario():
    return render_template('/Editar_Usuario.html')

@app.route("/Editar_Comentario", methods=["GET", "POST"])
def editar_comentario():
    return render_template('/Editar_Comentario.html')

@app.route("/Crear_Usuario", methods=["GET", "POST"])
def crear_usuario():
    return render_template('/Crear_Usuario.html')

@app.route("/Consultar_Usuario", methods=["GET", "POST"])
def consultar_usuario():
    return render_template('/Consultar_Usuario.html')

@app.route("/Consultar_Publicacion", methods=["GET", "POST"])
def consultar_publicacion():
    return render_template('/Consultar_Publicacion.html')

@app.route("/Consultar_Comentario", methods=["GET", "POST"])
def consultar_comentario():
    return render_template('/Consultar_Comentario.html')

@app.route("/Calificar_Publicacion", methods=["GET", "POST"])
def calificar_publicacion():
    return render_template('/Calificar_Publicacion.html')

if __name__=="__main__":
    app.run(debug=True)