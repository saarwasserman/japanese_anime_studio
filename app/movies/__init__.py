from flask import Blueprint


movies_bp = Blueprint('movies', __name__)


from . import api  # noqa - that is the intention of the import
from . import commands  # noqa
