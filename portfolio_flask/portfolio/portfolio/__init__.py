from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

from portfolio import routes
from portfolio.settings import db
