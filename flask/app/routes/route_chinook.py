from flask import Blueprint, render_template
from models.models import Artist, Album
from database import db

chinook_page = Blueprint("chinook_page", __name__)

@chinook_page.route('/artists')
def artists():
    artists = Artist.query.all()
    return render_template('chinook/index.html', data=artists, name="Artistes")

@chinook_page.route('/albums')
def albums():
    albums = Album.query.all()
    return render_template('chinook/index.html', data=albums, name="Albums")

@chinook_page.route('/artists_with_albums')
def artists_with_albums():
    artists_albums = Artist.query.join(Album).all()
    return render_template('chinook/index.html', data=artists_albums, name="Artistes avec Album")
