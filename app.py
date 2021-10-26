from flask import Flask, render_template, request, flash

app=Flask(__name__)

@app.route("/", methods=["GET"])
def inicio():
    return render_template('/index.html')

@app.route("/sign_up", methods=["GET", "POST"])
def signup():
    return render_template('/sign_up.html')

@app.route("/sign_in", methods=["GET", "POST"])
def login():
    return render_template('sign_in.html')

@app.route("/feed", methods=["GET"])
def feed():
    return render_template('/feed.html')

@app.route("/publicacion/<id_publicacion>", methods=["GET"])
def publicacion(id_publicacion):
    return render_template('/detalles-publicacion.html')

@app.route("/perfil_usuario", methods=["GET", "POST"])
def perfil_usuario():
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