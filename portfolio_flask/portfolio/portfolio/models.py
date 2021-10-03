from .settings import db


class Projeto(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    titulo = db.Column(
        db.String,
        unique=True,
        nullable=False
    )

    capa = db.Column(
        db.String,
        nullable=False,
        unique=True,
    )

    iframe_video = db.Column(
        db.Text,
        unique=True,
        nullable=False,
    )

    link_codigo = db.Column(
        db.String,
        nullable=False,
        unique=True,
    )

