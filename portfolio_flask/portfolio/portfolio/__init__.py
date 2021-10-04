from flask import Flask, redirect, render_template, url_for
from flask_migrate import Migrate

app = Flask(__name__)
## Importando as Settings do app
from .settings import *

## Configurando o modelo do bando de dados e criando o migrate
# -> "Flask db init; Flask db migrate"

from .model import configure as config_db
from .serealizer import configure as config_mb

config_db(app)
config_mb(app)
Migrate(app,app.db)

## Startando as rotas do app
from portfolio import routes

## Startando o banco de dados no app
from .model import db
