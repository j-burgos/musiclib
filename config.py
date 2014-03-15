
class DefaultConfig:
	DEBUG = False
	LISTEN_IP = '0.0.0.0'
	PORT = 80
	SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'

class DevConfig(DefaultConfig):
	DEBUG = True
	LISTEN_IP = '127.0.0.1'
	PORT = 5000
	SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'

class ProdConfig(DefaultConfig):
	DEBUG = False
	LISTEN_IP = '0.0.0.0'
	PORT = 80
	#Aqui podriamos configurar la cadena de conexion
	# para la base de datos ya real
	SQLALCHEMY_DATABASE_URI = 'engine://usuario:contrasenia@server:puerto/base_de_datos'