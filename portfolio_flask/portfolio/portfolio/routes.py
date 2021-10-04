import json
import os

from dotenv import load_dotenv
from flask import current_app, jsonify, render_template, request
from marshmallow.fields import Tuple

from portfolio import app

from .model import Projeto
from .projetos import bp_projetos
from .serealizer import ProjetoSchema

if os.path.exists("credentials.json"):
    with open("credentials.json") as file:
        data = json.load(file)
        api_token = data["API_KEY"]
else:
    load_dotenv()
    api_token = os.getenv("API_KEY")  ## Não passe sua chave API para ninguém


## API TOKEN
TOKEN = api_token


### HOME PAGE
@app.route("/")
def index():
    projetos = Projeto.query.all()
    return render_template("index.html", projetos=projetos)


### DETALHES DO PROJETO -> Video demonstrativo
@app.route("/video/projeto/<id>", methods=["GET"])
def detail_projeto(id):
    projeto = Projeto.query.filter(Projeto.id == id).first()
    return render_template("projeto.html", projeto=projeto)
    


### API CRUD PROJETOS
@bp_projetos.route("/projetos", methods=["GET"])
def listar_projetos():
    pj = ProjetoSchema(many=True)
    result = Projeto.query.all()
    return pj.jsonify(result), 200


@bp_projetos.route("/projeto/deletar/<id>", methods=["GET"])
def need_token_delete(id):
    return jsonify(
        {
            "Projeto": f"{id=}",
            "action": "delete",
            "status": "unsuccessfully",
            "reason": "need token",
        }
    )


@bp_projetos.route("/projeto/deletar/<id>/<token>", methods=["GET"])
def deletar_projetos(id, token):
    if token != TOKEN:
        return jsonify(
            {
                "Projeto": f"{id=}",
                "action": "delete",
                "status": "unsuccessfully",
                "reason": "token wrong",
            }
        )
    Projeto.query.filter(Projeto.id == id).delete()
    current_app.db.session.commit()
    return jsonify(
        {"Projeto": f"{id=}", "action": "delete", "status": "Success"}
    )


@bp_projetos.route("/projeto/atualizar/<id>", methods=["PATCH", "POST"])
def need_token_update(id):
    return jsonify(
        {
            "Projeto": f"{id=}",
            "action": "delete",
            "status": "unsuccessfully",
            "reason": "need token",
        }
    )


@bp_projetos.route(
    "/projeto/atualizar/<id>/<token>", methods=["PATCH", "POST"]
)
def atualizar_projeto(id, token):
    if token != TOKEN:
        return jsonify(
            {
                "Projeto": f"{id=}",
                "action": "update",
                "status": "unsuccessfully",
                "reason": "token wrong",
            }
        )
    pj = ProjetoSchema()
    query = Projeto.query.filter(Projeto.id == id)
    query.update(request.json)
    current_app.db.session.commit()
    return pj.jsonify(query.first()), 201


@bp_projetos.route("/projeto/new", methods=["GET", "POST"])
def need_token_create(*args):
    return jsonify(
        {
            "action": "create",
            "status": "unsuccessfully",
            "reason": "need token",
        }
    )


@bp_projetos.route("/projeto/new/<token>", methods=["POST"])
def inserir_projetos(token):
    if token != TOKEN:
        return jsonify(
            {
                "action": "create",
                "status": "unsuccessfully",
                "reason": "token wrong",
            }
        )
    pj = ProjetoSchema()
    data = request.json
    if isinstance(pj.load(data), Projeto):
        projeto = pj.load(data)
        current_app.db.session.add(projeto)
        current_app.db.session.commit()
    return pj.jsonify(projeto), 201
