Project
=======

Load movies list from ghibli movie site efficiently using redis for caching.

https://ghibliapi.herokuapp.com/#section/Studio-Ghibli-API



Instructions
------------

    1. cd to git repo
    2. docker-compose up
    3. Go to: http://localhost:8000/movies

Note: http://localhost:8000/api/movies will give you json


Tests: sudo docker exec -it ghibli_web_1 pytest

Linter: sudo docker exec -it ghibli_web_1 pycodestyle
	

Environments:
-------------
FLASK_CONFIG env var will control the environment. See config.py

options:

    development
    docker
    production

development is not using docker (redis should be installed on host)

Implementation:
---------------
Two methods to retrieve data from Ghibli Studio API:

    1. First request after 1 minute will retrieve the data (Default) 
    2. Cron - managed by flask custom commands and flask-crontab package. (should use both commands at the moment)


	To Enable (2):
    a. sudo docker exec -it ghibli_web_1 flask crontab add
    b. sudo docker exec -it ghibli_web_1 flask movies enable_cron

    TO Disable (2) and move back to (1): 
    a. sudo docker exec -it ghibli_web_1 flask crontab remove
    b. sudo docker exec -it ghibli_web_1 flask movies \ disable_cron 


Dev Tools
---------
    1. Ubuntu 20.04
    2. Visual Code
    3. Visual code python extension (including pep8 linter - pycodestyle)
    4. Git + GitHub
    5. Python 3.8



Software Stack:
--------------
    1. Alpine Linux os on Docker - python:3.8-alpine
    2. Web Framework - Flask
    3. Test Framework - Pytest
    4. Package and virtual env manager - Poetry
    5. Storage - Redis (In-memory)
