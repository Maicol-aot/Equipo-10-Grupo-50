from flask import Flask, render_template, request, flash

app=Flask(__name__)

@app.route("/", methods=["GET"])
def inicio():
    return render_template('/index.html')

@app.route("/signup", methods=["GET", "POST"])
def signup():
    return render_template('/sign_up.html')

@app.route("/login", methods=["GET", "POST"])
def ingreso():
    return render_template('sign_in.html')

@app.route("/feed", methods=["GET"])
def feed():
    return render_template('/feed.html')

@app.route("/publicacion", methods=["GET"])
def publicacion():
    return render_template('/detalles-publicacion.html')

@app.route("/administrador", methods=["GET", "POST"])
def administrador():
    return render_template('/administrador.html')

if __name__=="__main__":
    app.run(debug=True)