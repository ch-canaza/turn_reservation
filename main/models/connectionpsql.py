from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import psycopg2


app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:password@172.17.0.1:5432/postgres"
db = SQLAlchemy(app)
CORS(app)
migrate = Migrate(app, db)
