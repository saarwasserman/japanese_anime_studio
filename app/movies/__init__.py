from flask import Blueprint

movies_api = Blueprint('movies', __name__)

from . import api
