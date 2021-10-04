from flask_marshmallow import Marshmallow
from flask_marshmallow.sqla import SQLAlchemyAutoSchema
from marshmallow.utils import EXCLUDE
from .model import Projeto

ma = Marshmallow()

def configure(app):
	ma.init_app(app)

class ProjetoSchema(ma.SQLAlchemySchema):
	class Meta:
		model = Projeto
		unknown = EXCLUDE
		load_instance = True
		fields = ('id','titulo', 'capa', 'iframe_video', 'link_codigo')