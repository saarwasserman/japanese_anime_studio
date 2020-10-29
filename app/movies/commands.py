
from flask import current_app


import click
import redis
from flask import Blueprint


from . import movies_bp


from . import tasks
from .. import crontab


@movies_bp.cli.command('update')
def update_movies():
    """ update movie list """

    tasks.update_movies()


@movies_bp.cli.command('delete')
def delete_movies_list():
    """ delete movies data """

    with redis.Redis(host=current_app.config["REDIS_URL"]) as redis_connection:
        redis_connection.delete("ghibli")


@movies_bp.cli.command('enable_cron')
def enable_cron():
    """ delete movies data """

    with redis.Redis(host=current_app.config["REDIS_URL"]) as redis_connection:
        redis_connection.set("use_cron", 1)


@movies_bp.cli.command('disable_cron')
def disable_cron():
    """ delete movies data """

    with redis.Redis(host=current_app.config["REDIS_URL"]) as redis_connection:
        redis_connection.set("use_cron", 0)
