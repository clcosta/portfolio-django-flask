from portfolio import app

app.config['SECRET_KEY'] = '09ee04b84fc489acb2e52ef7f07461d170b6c62a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

## Registrando o serializador do DB
from .projetos import bp_projetos
app.register_blueprint(bp_projetos)
