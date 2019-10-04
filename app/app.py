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

class ConfigSites(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	foto_principal = db.Column(db.String(200))
	nombre = db.Column(db.String(200))
	slogan = db.Column(db.String(200))
	descripcion = db.Column(db.String(1000))
	email = db.Column(db.String(200))
	facebook = db.Column(db.String(200))
	twitter = db.Column(db.String(200))
	instagram = db.Column(db.String(200))
	color = db.Column(db.String(15))

class Fotos(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	titulo = db.Column(db.String(200))
	url = db.Column(db.String(200))
	descripcion = db.Column(db.String(1000))

db.init_app(app)
db.create_all()

@app.route('/')
def index():
	config = ConfigSites.query.first()

	if config and config.foto_principal:
		foto_principal = config.foto_principal
	else:
		foto_principal = 'https://icon-library.net/images/avatar-icon-png/avatar-icon-png-8.jpg'

	if config and config.nombre:
		nombre = config.nombre
	else:
		nombre = 'NOMBRE CANDIDATO'

	if config and config.slogan:
		slogan = config.slogan
	else:
		slogan = 'Slogan de Campaña'

	if config and config.descripcion:
		descripcion = config.descripcion
	else:
		descripcion = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

	if config and config.facebook:
		facebook = config.facebook
	else:
		facebook = '#'

	if config and config.twitter:
		twitter = config.twitter
	else:
		twitter = '#'

	if config and config.instagram:
		instagram = config.instagram
	else:
		instagram = '#'

	if config and config.color:
		color_fondo = config.color
	else:
		color_fondo = '#1abc9c'

	#Fotos
	foto_1 = Fotos.query.filter_by(id=1).first()
	foto_2 = Fotos.query.filter_by(id=2).first()
	foto_3 = Fotos.query.filter_by(id=3).first()
	foto_4 = Fotos.query.filter_by(id=4).first()
	foto_5 = Fotos.query.filter_by(id=5).first()
	foto_6 = Fotos.query.filter_by(id=6).first()

	pic_1 = Fotos()
	pic_2 = Fotos()
	pic_3 = Fotos()
	pic_4 = Fotos()
	pic_5 = Fotos()
	pic_6 = Fotos()

	if foto_1 and foto_1.titulo and foto_1.url and foto_1.descripcion:
		pic_1.titulo = foto_1.titulo
		pic_1.url = foto_1.url
		pic_1.descripcion = foto_1.descripcion
	else:
		pic_1.titulo = 'TITULO PUBLICACION'
		pic_1.url = 'https://www.pngkey.com/png/full/34-345766_crowd-clipart-person-icon-people-round-icon-png.png'
		pic_1.descripcion = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia neque assumenda ipsam nihil, molestias magnam, recusandae quos quis inventore quisquam velit asperiores, vitae? Reprehenderit soluta, eos quod consequuntur itaque. Nam.'

	if foto_2 and foto_2.titulo and foto_2.url and foto_2.descripcion:
		pic_2.titulo = foto_2.titulo
		pic_2.url = foto_2.url
		pic_2.descripcion = foto_2.descripcion
	else:
		pic_2.titulo = 'TITULO PUBLICACION'
		pic_2.url = 'https://www.pngkey.com/png/full/34-345766_crowd-clipart-person-icon-people-round-icon-png.png'
		pic_2.descripcion = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia neque assumenda ipsam nihil, molestias magnam, recusandae quos quis inventore quisquam velit asperiores, vitae? Reprehenderit soluta, eos quod consequuntur itaque. Nam.'

	if foto_3 and foto_3.titulo and foto_3.url and foto_3.descripcion:
		pic_3.titulo = foto_3.titulo
		pic_3.url = foto_3.url
		pic_3.descripcion = foto_3.descripcion
	else:
		pic_3.titulo = 'TITULO PUBLICACION'
		pic_3.url = 'https://www.pngkey.com/png/full/34-345766_crowd-clipart-person-icon-people-round-icon-png.png'
		pic_3.descripcion = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia neque assumenda ipsam nihil, molestias magnam, recusandae quos quis inventore quisquam velit asperiores, vitae? Reprehenderit soluta, eos quod consequuntur itaque. Nam.'

	if foto_4 and foto_4.titulo and foto_4.url and foto_4.descripcion:
		pic_4.titulo = foto_4.titulo
		pic_4.url = foto_4.url
		pic_4.descripcion = foto_4.descripcion
	else:
		pic_4.titulo = 'TITULO PUBLICACION'
		pic_4.url = 'https://www.pngkey.com/png/full/34-345766_crowd-clipart-person-icon-people-round-icon-png.png'
		pic_4.descripcion = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia neque assumenda ipsam nihil, molestias magnam, recusandae quos quis inventore quisquam velit asperiores, vitae? Reprehenderit soluta, eos quod consequuntur itaque. Nam.'

	if foto_5 and foto_5.titulo and foto_5.url and foto_5.descripcion:
		pic_5.titulo = foto_5.titulo
		pic_5.url = foto_5.url
		pic_5.descripcion = foto_5.descripcion
	else:
		pic_5.titulo = 'TITULO PUBLICACION'
		pic_5.url = 'https://www.pngkey.com/png/full/34-345766_crowd-clipart-person-icon-people-round-icon-png.png'
		pic_5.descripcion = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia neque assumenda ipsam nihil, molestias magnam, recusandae quos quis inventore quisquam velit asperiores, vitae? Reprehenderit soluta, eos quod consequuntur itaque. Nam.'

	if foto_6 and foto_6.titulo and foto_6.url and foto_6.descripcion:
		pic_6.titulo = foto_6.titulo
		pic_6.url = foto_6.url
		pic_6.descripcion = foto_6.descripcion
	else:
		pic_6.titulo = 'TITULO PUBLICACION'
		pic_6.url = 'https://www.pngkey.com/png/full/34-345766_crowd-clipart-person-icon-people-round-icon-png.png'
		pic_6.descripcion = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia neque assumenda ipsam nihil, molestias magnam, recusandae quos quis inventore quisquam velit asperiores, vitae? Reprehenderit soluta, eos quod consequuntur itaque. Nam.'

	return render_template('index.html', nombre=nombre, slogan=slogan, foto_principal=foto_principal, descripcion=descripcion, facebook=facebook, twitter=twitter, instagram=instagram, color_fondo=color_fondo, pic_1=pic_1, pic_2=pic_2, pic_3=pic_3, pic_4=pic_4, pic_5=pic_5, pic_6=pic_6 )

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
