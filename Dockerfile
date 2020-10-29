FROM python:3.8-alpine

# code workspace
WORKDIR /code
COPY ./ /code/

# system deps
RUN apk add curl

# poetry and python package requirements
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - \
    && source $HOME/.poetry/env \
    && poetry config virtualenvs.create false \
    && poetry install

EXPOSE 8000

CMD ["flask", "run", "--host", "0.0.0.0"]

