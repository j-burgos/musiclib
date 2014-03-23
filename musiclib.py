from flask import Flask, render_template
from models import Artist

app = Flask(__name__)

@app.route('/')
def index():
	response = ""
	artists = Artist.query.all()
	for artist in artists:
		response += '<div>'
		response += '<h1>' + artist.name + '</h1>'
		response += '<ul>'
		for album in artist.albums:
			response += '<li>' + album.name + '</li>'
			response += '<ol>'
			for song in album.songs:
					response += '<li>' + song.name + '</li>'
			response += '</ol>'
		response += '</ul>'
		response += '</div>'
	return render_template('index.html')