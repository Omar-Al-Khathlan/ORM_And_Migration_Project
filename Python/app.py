from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from configparser import ConfigParser
from models.models import db


config = ConfigParser()
config.read('config.ini')

db_config = config['DATABASE']


app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://{}:{}@{}/{}'.format(db_config['DB_USER'],
                                                                                   db_config['DB_PASSWORD'],
                                                                                   db_config['DB_HOST'],
                                                                                   db_config['DB_NAME'])
db.init_app(app)
migrate = Migrate(app, db)

