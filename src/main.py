#this is for unittests just ignore this for now

import unittest
import os
import re
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask import Marshmallow

def add(a, b):
    #add function is a dummy test
    return (a + b)

db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object("default_settings.app_config")

    if app.config["ENV"] == "production":
        from log_handlers import file_handler
        app.logger.addHandler(file_handler)
