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

def initial_config():
	if Usuarios.query.filter_by(usuario="admin").first() is None:
		contrasena_encriptada = generate_password_hash("123456", method='sha256')
		nuevo_usuario = Usuarios(usuario="admin",contrasena=contrasena_encriptada)
		db.session.add(nuevo_usuario)
		db.session.commit()

	if ConfigSites.query.first() is None:
		nuevo_sitio = ConfigSites(foto_principal = 'https://icon-library.net/images/avatar-icon-png/avatar-icon-png-8.jpg', nombre = 'NOMBRE CANDIDATO', slogan = 'Slogan de Campaña', descripcion = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', facebook = '#', twitter = '#', instagram = '#', color = '#1abc9c')
		db.session.add(nuevo_sitio)
		db.session.commit()

	if Fotos.query.first() is None:
		nueva_foto_1 = Fotos(titulo ='TITULO PUBLICACION', url ='https://www.pngkey.com/png/full/34-345766_crowd-clipart-person-icon-people-round-icon-png.png', descripcion ='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia neque assumenda ipsam nihil, molestias magnam, recusandae quos quis inventore quisquam velit asperiores, vitae? Reprehenderit soluta, eos quod consequuntur itaque. Nam.')
		db.session.add(nueva_foto_1)
		db.session.commit()
		nueva_foto_2 = Fotos(titulo ='TITULO PUBLICACION', url ='https://www.pngkey.com/png/full/34-345766_crowd-clipart-person-icon-people-round-icon-png.png', descripcion ='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia neque assumenda ipsam nihil, molestias magnam, recusandae quos quis inventore quisquam velit asperiores, vitae? Reprehenderit soluta, eos quod consequuntur itaque. Nam.')
		db.session.add(nueva_foto_2)
		db.session.commit()
		nueva_foto_3 = Fotos(titulo ='TITULO PUBLICACION', url ='https://www.pngkey.com/png/full/34-345766_crowd-clipart-person-icon-people-round-icon-png.png', descripcion ='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia neque assumenda ipsam nihil, molestias magnam, recusandae quos quis inventore quisquam velit asperiores, vitae? Reprehenderit soluta, eos quod consequuntur itaque. Nam.')
		db.session.add(nueva_foto_3)
		db.session.commit()
		nueva_foto_4 = Fotos(titulo ='TITULO PUBLICACION', url ='https://www.pngkey.com/png/full/34-345766_crowd-clipart-person-icon-people-round-icon-png.png', descripcion ='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia neque assumenda ipsam nihil, molestias magnam, recusandae quos quis inventore quisquam velit asperiores, vitae? Reprehenderit soluta, eos quod consequuntur itaque. Nam.')
		db.session.add(nueva_foto_4)
		db.session.commit()
		nueva_foto_5 = Fotos(titulo ='TITULO PUBLICACION', url ='https://www.pngkey.com/png/full/34-345766_crowd-clipart-person-icon-people-round-icon-png.png', descripcion ='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia neque assumenda ipsam nihil, molestias magnam, recusandae quos quis inventore quisquam velit asperiores, vitae? Reprehenderit soluta, eos quod consequuntur itaque. Nam.')
		db.session.add(nueva_foto_5)
		db.session.commit()
		nueva_foto_6 = Fotos(titulo ='TITULO PUBLICACION', url ='https://www.pngkey.com/png/full/34-345766_crowd-clipart-person-icon-people-round-icon-png.png', descripcion ='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia neque assumenda ipsam nihil, molestias magnam, recusandae quos quis inventore quisquam velit asperiores, vitae? Reprehenderit soluta, eos quod consequuntur itaque. Nam.')
		db.session.add(nueva_foto_6)
		db.session.commit()


@app.route('/')
def index():
	initial_config()

	config = ConfigSites.query.first()

	foto_principal = config.foto_principal
	nombre = config.nombre
	slogan = config.slogan
	descripcion = config.descripcion
	facebook = config.facebook
	twitter = config.twitter
	instagram = config.instagram
	color_fondo = config.color

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

	pic_1.titulo = foto_1.titulo
	pic_1.url = foto_1.url
	pic_1.descripcion = foto_1.descripcion

	pic_2.titulo = foto_2.titulo
	pic_2.url = foto_2.url
	pic_2.descripcion = foto_2.descripcion

	pic_3.titulo = foto_3.titulo
	pic_3.url = foto_3.url
	pic_3.descripcion = foto_3.descripcion

	pic_4.titulo = foto_4.titulo
	pic_4.url = foto_4.url
	pic_4.descripcion = foto_4.descripcion

	pic_5.titulo = foto_5.titulo
	pic_5.url = foto_5.url
	pic_5.descripcion = foto_5.descripcion

	pic_6.titulo = foto_6.titulo
	pic_6.url = foto_6.url
	pic_6.descripcion = foto_6.descripcion

	return render_template('index.html', nombre=nombre, slogan=slogan, foto_principal=foto_principal, descripcion=descripcion, facebook=facebook, twitter=twitter, instagram=instagram, color_fondo=color_fondo, pic_1=pic_1, pic_2=pic_2, pic_3=pic_3, pic_4=pic_4, pic_5=pic_5, pic_6=pic_6 )

@app.route('/py_admin', methods=['GET', 'POST'])
def py_admin():
	if "usuario" in session:
		if request.method == 'POST':
			config = ConfigSites.query.first()
			config.foto_principal = request.form['foto_principal']
			config.nombre = request.form['nombre']
			config.slogan = request.form['slogan']
			config.descripcion = request.form['descripcion']
			config.facebook = request.form['facebook']
			config.twitter = request.form['twitter']
			config.instagram = request.form['instagram']
			config.color = request.form['color_fondo']

			foto_1 = Fotos.query.filter_by(id=1).first()
			foto_2 = Fotos.query.filter_by(id=2).first()
			foto_3 = Fotos.query.filter_by(id=3).first()
			foto_4 = Fotos.query.filter_by(id=4).first()
			foto_5 = Fotos.query.filter_by(id=5).first()
			foto_6 = Fotos.query.filter_by(id=6).first()

			foto_1.titulo = request.form['pic_1_title']
			foto_1.url = request.form['pic_1_url']
			foto_1.descripcion = request.form['pic_1_descripcion']

			foto_2.titulo = request.form['pic_2_title']
			foto_2.url = request.form['pic_2_url']
			foto_2.descripcion = request.form['pic_2_descripcion']

			foto_3.titulo = request.form['pic_3_title']
			foto_3.url = request.form['pic_3_url']
			foto_3.descripcion = request.form['pic_3_descripcion']

			foto_4.titulo = request.form['pic_4_title']
			foto_4.url = request.form['pic_4_url']
			foto_4.descripcion = request.form['pic_4_descripcion']

			foto_5.titulo = request.form['pic_5_title']
			foto_5.url = request.form['pic_5_url']
			foto_5.descripcion = request.form['pic_5_descripcion']

			foto_6.titulo = request.form['pic_6_title']
			foto_6.url = request.form['pic_6_url']
			foto_6.descripcion = request.form['pic_6_descripcion']

			db.session.flush()
			db.session.commit()

			return index()

		config = ConfigSites.query.first()

		foto_principal = config.foto_principal
		nombre = config.nombre
		slogan = config.slogan
		descripcion = config.descripcion
		facebook = config.facebook
		twitter = config.twitter
		instagram = config.instagram
		color_fondo = config.color

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

		pic_1.titulo = foto_1.titulo
		pic_1.url = foto_1.url
		pic_1.descripcion = foto_1.descripcion

		pic_2.titulo = foto_2.titulo
		pic_2.url = foto_2.url
		pic_2.descripcion = foto_2.descripcion

		pic_3.titulo = foto_3.titulo
		pic_3.url = foto_3.url
		pic_3.descripcion = foto_3.descripcion

		pic_4.titulo = foto_4.titulo
		pic_4.url = foto_4.url
		pic_4.descripcion = foto_4.descripcion

		pic_5.titulo = foto_5.titulo
		pic_5.url = foto_5.url
		pic_5.descripcion = foto_5.descripcion

		pic_6.titulo = foto_6.titulo
		pic_6.url = foto_6.url
		pic_6.descripcion = foto_6.descripcion

		return render_template('py_admin.html', nombre=nombre, slogan=slogan, foto_principal=foto_principal, descripcion=descripcion, facebook=facebook, twitter=twitter, instagram=instagram, color_fondo=color_fondo, pic_1=pic_1, pic_2=pic_2, pic_3=pic_3, pic_4=pic_4, pic_5=pic_5, pic_6=pic_6 )
	return iniciar_sesion()



################################################################

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
			return py_admin()
		return "Los datos ingresados no son válidos"
	return render_template('iniciar_sesion.html')

if __name__ == '__main__':
	app.run(debug=True)
