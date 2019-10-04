from flask import Flask, render_template, request, session, make_response, escape
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.secret_key = '123456'

class Usuarios(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	usuario = db.Column(db.String(50), unique=True, nullable=True)
	contrasena = db.Column(db.String(80), nullable=True)

class ConfigSite(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	foto_principal = db.Column(db.String(200))
	nombre = db.Column(db.String(200))
	slogan = db.Column(db.String(200))
	descripcion = db.Column(db.String(1000))
	email = db.Column(db.String(200))
	facebook = db.Column(db.String(200))
	twitter = db.Column(db.String(200))
	instagram = db.Column(db.String(200))

class Fotos(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	titulo = db.Column(db.String(200))
	url = db.Column(db.String(200))
	descripcion = db.Column(db.String(1000))

db.init_app(app)
db.create_all()

@app.route('/')
def index():
	config = ConfigSite.query.filter_by(id=1).first()

	if config.foto_principal:
		foto_principal = config.foto_principal
	else:
		foto_principal = 'https://icon-library.net/images/avatar-icon-png/avatar-icon-png-8.jpg'

	if config.nombre:
		nombre = config.nombre
	else:
		nombre = 'NOMBRE CANDIDATO'

	if config.slogan:
		slogan = config.slogan
	else:
		slogan = 'Slogan de Campaña'

	if config.descripcion:
		descripcion = config.descripcion
	else:
		descripcion = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

	#agregar Fotos

	return render_template('index.html', nombre=nombre, slogan=slogan, foto_principal=foto_principal, descripcion=descripcion)

@app.route('/py_admin')
def py_admin():
	if "usuario" in session:
		return "Estas logueado %s" % escape(session['usuario'])
	return render_template('iniciar_sesion.html')

################################################################

@app.route('/buscar')
def buscar():
	pass

def validar_datos(usuario):
	if len(usuario) <= 5:
		return "Usuario No Válido"

@app.route('/registrarse', methods=['GET', 'POST'])
def registrarse():
	if request.method == 'POST':
		usuario = request.form['usuario']
		contrasena = request.form['contrasena']

		contrasena_encriptada = generate_password_hash(contrasena,method='sha256')
		nuevo_usuario = Usuarios(usuario=usuario,contrasena=contrasena_encriptada)
		db.session.add(nuevo_usuario)
		db.session.commit()
		return "Usuario registrado"
	return render_template('registrarse.html')

@app.route('/iniciar_sesion', methods=['GET', 'POST'])
def iniciar_sesion():
	if request.method == 'POST':
		usuario = request.form['usuario']
		contrasena = request.form['contrasena']
		usuario = Usuarios.query.filter_by(usuario=usuario).first()

		if usuario and check_password_hash(usuario.contrasena,contrasena):
			session['usuario'] = usuario.usuario
			return "Inicio de Sesión Exitoso"
		return "Los datos ingresados no son válidos"
	return render_template('iniciar_sesion.html')

@app.route('/home')
def home():
	if "usuario" in session:
		return "Estas logueado %s" % escape(session['usuario'])
	return "debes iniciar sesión"


if __name__ == '__main__':
	db.create_all()
	app.run(debug=True)
