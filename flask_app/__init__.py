from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = '241a5678b58a0003493405096d3de573'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' 

from flask_app import routes