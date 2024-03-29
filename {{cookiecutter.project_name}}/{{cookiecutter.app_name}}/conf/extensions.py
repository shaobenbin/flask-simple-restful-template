# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located in app.py."""
from flask_bcrypt import Bcrypt
from flask_caching import Cache
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_seasurf import SeaSurf

bcrypt = Bcrypt()
csrf_protect = SeaSurf()
login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()
cache = Cache()
