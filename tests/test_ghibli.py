from datetime import datetime
from time import sleep

from redis import Redis
import pytest
import requests

from ghibli import app
from app import __version__
from app.movies.tasks import get_movies
from app.movies import tasks

from . import shell


UPDATE_URL = "http://localhost:8000/api/movies/update"
GET_MOVIES_URL = "http://localhost:8000/api/movies"


def test_version():
    "check version is up to date"

    assert __version__ == '0.1.0'


def test_movies_retrieval():
    """check if movies data from ghibli studio was received"""

    requests.post(url=UPDATE_URL)
    res = requests.get(url=GET_MOVIES_URL)
    assert res.status_code == 200

    data = res.json()
    assert len(data) >= 20


def test_data_retrieval_within_the_minute():
    """check update doesn't occur within the 1 minute
       delete data and assert no data is retreivable
    """

    redis_conn = Redis(app.config["REDIS_URL"])

    # first call
    requests.post(url=UPDATE_URL)
    res = requests.get(url=GET_MOVIES_URL)
    assert res.status_code == 200

    redis_conn.delete("ghibli")

    # second call
    res = requests.get(url=GET_MOVIES_URL)
    assert res.status_code != 200

    redis_conn.close()


def test_data_retrieval_beyond_the_minute():
    """check update occur after 1 minute
       delete data and check data is retreivable after interval
    """

    redis_conn = Redis(app.config["REDIS_URL"])
    requests.post(url=UPDATE_URL)
    # first call
    res = requests.get(url=GET_MOVIES_URL)
    assert res.status_code == 200

    redis_conn.delete("ghibli")

    # update of DB should occur after 1 minute
    sleep(app.config["MOVIES_UPDATE_INTERVAL"] + 10)

    # second call
    res = requests.get(url=GET_MOVIES_URL)
    assert res.status_code == 200

    redis_conn.close()

# !!! Test the same for cron


@pytest.mark.skip()
def test_new_data_in_db():
    """use local custom db
    """
    # 5 movies db
    # add movie
    # wait 1 minute
    # retrieve data
    # assert len(movies) == 6
    pass
