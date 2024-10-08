from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class MediaType(db.Model):
    __tablename__ = 'media_types'
    MediaTypeId: Mapped[int] = mapped_column(primary_key=True)
    Name: Mapped[str] = mapped_column(String(120), nullable=False)

class Genre(db.Model):
    __tablename__ = 'genres'
    GenreId: Mapped[int] = mapped_column(primary_key=True)
    Name: Mapped[str] = mapped_column(String(120), nullable=False)

class Artist(db.Model):
    __tablename__ = 'artists'
    ArtistId: Mapped[int] = mapped_column(primary_key=True)
    Name: Mapped[str] = mapped_column(String(120), nullable=False)

    albums: Mapped[list['Album']] = relationship('Album', backref='artist', lazy=True)

class Album(db.Model):
    __tablename__ = 'albums'
    AlbumId: Mapped[int] = mapped_column(primary_key=True)
    Title: Mapped[str] = mapped_column(String(160), nullable=False)
    ArtistId: Mapped[int] = mapped_column(ForeignKey('artists.ArtistId'), nullable=False)

    tracks: Mapped[list['Track']] = relationship('Track', backref='album', lazy=True)

class Track(db.Model):
    __tablename__ = 'tracks'
    TrackId: Mapped[int] = mapped_column(primary_key=True)
    Name: Mapped[str] = mapped_column(String(200), nullable=False)
    AlbumId: Mapped[int] = mapped_column(ForeignKey('albums.AlbumId'), nullable=True)
    MediaTypeId: Mapped[int] = mapped_column(ForeignKey('media_types.MediaTypeId'), nullable=False)
    GenreId: Mapped[int] = mapped_column(ForeignKey('genres.GenreId'), nullable=True)
    Composer: Mapped[str] = mapped_column(String(220), nullable=True)
    Milliseconds: Mapped[int] = mapped_column(nullable=False)
    Bytes: Mapped[int] = mapped_column(nullable=True)
    UnitPrice: Mapped[float] = mapped_column(nullable=False)

    media_type: Mapped['MediaType'] = relationship('MediaType', backref='tracks', lazy=True)
    genre: Mapped['Genre'] = relationship('Genre', backref='tracks', lazy=True)

class Playlist(db.Model):
    __tablename__ = 'playlists'
    PlaylistId: Mapped[int] = mapped_column(primary_key=True)
    Name: Mapped[str] = mapped_column(String(120), nullable=False)

    tracks: Mapped[list['PlaylistTrack']] = relationship('PlaylistTrack', backref='playlist', lazy=True)

class PlaylistTrack(db.Model):
    __tablename__ = 'playlist_track'
    PlaylistId: Mapped[int] = mapped_column(ForeignKey('playlists.PlaylistId'), primary_key=True)
    TrackId: Mapped[int] = mapped_column(ForeignKey('tracks.TrackId'), primary_key=True)

    track: Mapped['Track'] = relationship('Track', backref='playlist_tracks', lazy=True)

class Customer(db.Model):
    __tablename__ = 'customers'
    CustomerId: Mapped[int] = mapped_column(primary_key=True)
    FirstName: Mapped[str] = mapped_column(String(40), nullable=False)
    LastName: Mapped[str] = mapped_column(String(20), nullable=False)
    Company: Mapped[str] = mapped_column(String(80), nullable=True)
    Address: Mapped[str] = mapped_column(String(70), nullable=False)
    City: Mapped[str] = mapped_column(String(40), nullable=False)
    State: Mapped[str] = mapped_column(String(40), nullable=True)
    Country: Mapped[str] = mapped_column(String(40), nullable=False)
    PostalCode: Mapped[str] = mapped_column(String(10), nullable=True)
    Phone: Mapped[str] = mapped_column(String(24), nullable=True)
    Fax: Mapped[str] = mapped_column(String(24), nullable=True)
    Email: Mapped[str] = mapped_column(String(60), nullable=False)
    SupportRepId: Mapped[int] = mapped_column(ForeignKey('employees.EmployeeId'), nullable=True)

    support_rep: Mapped['Employee'] = relationship('Employee', backref='customers', lazy=True)

class Invoice(db.Model):
    __tablename__ = 'invoices'
    InvoiceId: Mapped[int] = mapped_column(primary_key=True)
    CustomerId: Mapped[int] = mapped_column(ForeignKey('customers.CustomerId'), nullable=False)
    InvoiceDate: Mapped[datetime] = mapped_column(nullable=False)
    BillingAddress: Mapped[str] = mapped_column(String(70), nullable=True)
    BillingCity: Mapped[str] = mapped_column(String(40), nullable=True)
    BillingState: Mapped[str] = mapped_column(String(40), nullable=True)
    BillingCountry: Mapped[str] = mapped_column(String(40), nullable=True)
    BillingPostalCode: Mapped[str] = mapped_column(String(10), nullable=True)

    customer: Mapped['Customer'] = relationship('Customer', backref='invoices', lazy=True)

class InvoiceItem(db.Model):
    __tablename__ = 'invoice_items'
    InvoiceItemId: Mapped[int] = mapped_column(primary_key=True)
    InvoiceId: Mapped[int] = mapped_column(ForeignKey('invoices.InvoiceId'), nullable=False)
    TrackId: Mapped[int] = mapped_column(ForeignKey('tracks.TrackId'), nullable=False)
    UnitPrice: Mapped[float] = mapped_column(nullable=False)
    Quantity: Mapped[int] = mapped_column(nullable=False)

    invoice: Mapped['Invoice'] = relationship('Invoice', backref='invoice_items', lazy=True)
    track: Mapped['Track'] = relationship('Track', backref='invoice_items', lazy=True)

class Employee(db.Model):
    __tablename__ = 'employees'
    EmployeeId: Mapped[int] = mapped_column(primary_key=True)
    LastName: Mapped[str] = mapped_column(String(20), nullable=False)
    FirstName: Mapped[str] = mapped_column(String(40), nullable=False)
    Title: Mapped[str] = mapped_column(String(30), nullable=True)
    ReportsTo: Mapped[int] = mapped_column(ForeignKey('employees.EmployeeId'), nullable=True)
    BirthDate: Mapped[datetime] = mapped_column(nullable=True)
    HireDate: Mapped[datetime] = mapped_column(nullable=False)
    Address: Mapped[str] = mapped_column(String(70), nullable=False)
    City: Mapped[str] = mapped_column(String(40), nullable=False)
    State: Mapped[str] = mapped_column(String(40), nullable=True)
    Country: Mapped[str] = mapped_column(String(40), nullable=False)
    PostalCode: Mapped[str] = mapped_column(String(10), nullable=True)
    Phone: Mapped[str] = mapped_column(String(24), nullable=True)
    Fax: Mapped[str] = mapped_column(String(24), nullable=True)
    Email: Mapped[str] = mapped_column(String(60), nullable=False)

    manager: Mapped['Employee'] = relationship('Employee', remote_side=[EmployeeId], backref='subordinates', lazy=True)
