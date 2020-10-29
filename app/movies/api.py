from flask import jsonify, render_template


from . import movies_bp
from . import tasks


@movies_bp.route("/", methods=["GET"])
def index():
    """retrieve updated movie list"""

    return "Hello Ghibli"


@movies_bp.route("/movies/", methods=["GET"])
def get_movies():
    """retrieve updated movie list"""

    movies_data = tasks.get_movies()
    return render_template("movies.html", movies_list=movies_data)


@movies_bp.route("/api/movies/", methods=["GET"])
def get_movies_api():
    """retrieve updated movie list"""

    movies_data = tasks.get_movies()
    return jsonify(movies_data)


@movies_bp.route("/api/movies/update", methods=["POST"])
def update_movies():
    """retrieve updated movie list"""

    movies_data = tasks.update_movies()
