
import logging
import json
from datetime import datetime, timedelta
from flask import current_app

from .. import crontab

import requests
import redis


logger = logging.getLogger(__name__)

LAST_MOVIES_REQUEST_DATETIME = datetime.min


def get_movies():
    """Retrieve movie list from ghibli studio, update 'cache' if necessary
    """

    global LAST_MOVIES_REQUEST_DATETIME

    with redis.Redis(host=current_app.config["REDIS_URL"]) as redis_connection:

        # fetch config for cron job for updating movies
        use_cron = int(redis_connection.get("use_cron"))
        if not use_cron:
            now = datetime.now()
            desired_delta = now - timedelta(seconds=current_app.config["MOVIES_UPDATE_INTERVAL"])  # noqa
            if LAST_MOVIES_REQUEST_DATETIME < desired_delta:
                LAST_MOVIES_REQUEST_DATETIME = now
                update_movies()
                current_app.logger.info("Retrieved data from Ghibli API")

        data = redis_connection.get("ghibli")

    current_app.logger.info("Retrieved data from redis")
    return json.loads(data)


def update_movies():

    ghibli_base_url = current_app.config["GHIBLI_BASE_URL"]
    # get all movies keys
    films = requests.get(url=f"{ghibli_base_url}/films")
    # TODO: add assertion and exception handling
    people = requests.get(url=f"{ghibli_base_url}/people")

    data = {}
    # preferred one call to /films api to get names of all films
    for film in films.json():
        data[film['id']] = {
            "movie_name": film["title"],
            "people": []
        }

    for participant in people.json():
        for film in participant["films"]:
            film_id = film.split('/')[-1]
            data[film_id]["people"].append(participant["name"])

    # redis
    with redis.Redis(host=current_app.config["REDIS_URL"]) as redis_conn:
        redis_conn.set("ghibli", json.dumps(data))


@crontab.job()  # default: every minute
def update_movies_list():
    update_movies()
    logger.info("upadted data in redis")
