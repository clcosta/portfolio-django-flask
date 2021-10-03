from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms.fields.core import StringField
from wtforms.fields.simple import TextField
from wtforms.validators import DataRequired


class ProjetoCreateWithForm(FlaskForm):
    titulo = StringField('TTitulo do Projeto', validators=[DataRequired()])
    iframe_video = TextField('Iframe (Vídeo) que será exibido na página!', validators=[DataRequired()])
    link_codigo = StringField('link do Código no GitHub', validators=[DataRequired()])
    capa = FileField('Selecione uma imagem para a Capa do Projeto', validators=[FileAllowed(['jpg','png','jpeg','webp'])])
