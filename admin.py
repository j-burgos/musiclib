from flask.ext.admin import Admin, BaseView, expose
from flask.ext.admin.contrib.sqla import ModelView
from models import db, Artist, Album, Song

admin = Admin(name='Music Library')

admin.add_view(ModelView(Artist, db.session))
admin.add_view(ModelView(Album, db.session))
admin.add_view(ModelView(Song, db.session))