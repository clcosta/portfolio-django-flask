from flask_sqlalchemy import SQLAlchemy

from portfolio import *

app.config['SECRET_KEY'] = '09ee04b84fc489acb2e52ef7f07461d170b6c62a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'

db = SQLAlchemy(app)
