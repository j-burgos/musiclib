from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Artist(db.Model):

	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(100), unique=True)

	albums = db.relationship('Album', backref='artist', lazy='dynamic', foreign_keys='Album.artist_id')
	
	def __init__(self,name):
		self.name = name
	def __repr__(self):
		return '<Artist {}>'.format(self.name)
	def __str__(self):
		pass

class Album(db.Model):

	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(100), unique=True)
	genre = db.Column(db.String(100), nullable=True)
	artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))

	songs = db.relationship('Song', backref='album', lazy='dynamic', foreign_keys='Song.album_id')
	
	def __init__(self,name,genre=None):
		self.name = name
		self.genre = genre
	def __repr__(self):
		return '<Album {}>'.format(self.name)
	def __str__(self):
		pass
	
class Song(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), unique=True)
	year = db.Column(db.Integer, nullable=True)
	album_id = db.Column(db.Integer, db.ForeignKey('album.id'))

	def __init__(self,name,year=None):
		self.name = name
		self.year = year
	def __repr__(self):
		return '<Song {}>'.format(self.name)
	def __str__(self):
		pass

