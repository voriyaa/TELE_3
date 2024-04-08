# blueprints/user_api/__init__.py
from flask import Blueprint

user = Blueprint('api', __name__, url_prefix='/user_api')