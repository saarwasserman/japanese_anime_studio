__version__ = '0.1.0'

from redis import Redis
from flask import Flask
import rq
import rq_scheduler

from config import config

def create_app(config_name):
    """ """
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # initiate app components
    app.redis = Redis.from_url(app.config["REDIS_URL"])
    app.task_queue = rq.Queue("", connection=app.redis)
    app.scheduler = rq_scheduler.Scheduler

    # register blueprints
    from .movies import movies_api as movies_api_blueprint
    app.register_blueprint(movies_api_blueprint)

    return app
