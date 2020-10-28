from flask import jsonify, render_template


from . import movies_api
from . import tasks


@movies_api.route("/", methods=["GET"])
def index():
    """retrieve updated movie list"""

    return "Hello Ghibli"


@movies_api.route("/movies/", methods=["GET"])
def get_movies():
    """retrieve updated movie list"""

    movies_data = tasks.get_movies()
    return render_template("movies.html", movies_list=movies_data)
