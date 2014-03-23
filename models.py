from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Artist(db.Model):

	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(100), unique=True)

	albums = db.relationship('Album', backref='artist', lazy='dynamic', foreign_keys='Album.artist_id')
	
	def __repr__(self):
		return '<Artist {}>'.format(self.name)
	def __str__(self):
		return self.name

class Album(db.Model):

	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(100), unique=True)
	genre = db.Column(db.String(100), nullable=True)
	artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))

	def __repr__(self):
		return '<Album {}>'.format(self.name)
	def __str__(self):
		return self.name
	
class Song(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), unique=True)
	year = db.Column(db.Integer, nullable=True)
	album_id = db.Column(db.Integer, db.ForeignKey('album.id'))

	album = db.relationship('Album', backref='songs')

	def __repr__(self):
		return '<Song {}>'.format(self.name)
	def __str__(self):
		return self.name

