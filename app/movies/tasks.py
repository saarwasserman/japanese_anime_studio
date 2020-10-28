
import json
from datetime import datetime
from flask import current_app

import requests
import redis

# from flask import jsonify, request, g, url_for, current_app

LAST_MOVIES_REQUEST_DATETIME = datetime.min


def get_movies():
    """
    """

    #  fetch config for cron job for updating movies
    # use_cron = current_app.config["MOVIES_USE_CRON"]

    # if not use_cron and LAST_REQUEST_DATETIME > timedelta 1 minute:
    #     LAST_MOVIES_REQUEST_DATETIME = datetiem.now()
    #     update_movies()

    update_movies()

    # fetch data from redis
    conn = redis.Redis(host='localhost')
    data = conn.get("ghibli")

    # TODO: add exception couldn't retrieve data
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

    # only add name of participant, could add all data and let frontend show what is need
    # size <-> latency tradeoff
    for participant in people.json():
        for film in participant["films"]:
            film_id = film.split('/')[-1]
            data[film_id]["people"].append(participant["name"])

    # redis
    conn = redis.Redis(host='localhost')
    conn.set("ghibli", json.dumps(data))


    print(data)
