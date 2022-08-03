# save this as app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)


# this is to import all the files inside routes.py
from routes import *

if __name__ == '__main__':
    app.run(port = 5050, debug = True)