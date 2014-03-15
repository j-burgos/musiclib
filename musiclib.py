from flask import Flask
from models import Artist

app = Flask(__name__)

@app.route('/')
def index():
	artists = Artist.query.all()
	print artists
	response = [artist.name for artist in artists]
	return '<br>'.join(response)