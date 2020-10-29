""" app initialization """

__version__ = '0.1.0'

import logging
from datetime import datetime

from flask import Flask
from flask_crontab import Crontab
from redis import Redis

from config import config


crontab = Crontab()


def create_app(config_name):
    """ init flask app instance """
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # initiate app components
    crontab.init_app(app)

    # logging
    log_level = logging.DEBUG if app.config["DEBUG"] else logging.INFO
    app.logger.setLevel(log_level)

    # register blueprints
    from .movies import movies_bp
    app.register_blueprint(movies_bp, cli_group="movies")

    # init runtime variables in redis
    with Redis(host=app.config["REDIS_URL"]) as redis_connection:

        redis_connection.set("use_cron", 0)
        redis_connection.set("request_interval", 1)

    return app
