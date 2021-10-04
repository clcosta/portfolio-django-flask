from flask import Blueprint

bp_projetos = Blueprint('projetos', __name__)

## levando o pb_projetos pro routes
from .routes import *