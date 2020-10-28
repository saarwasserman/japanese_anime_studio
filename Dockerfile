FROM python:3.8-alpine

WORKDIR /code
ENV FLASK_APP=ghibli.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers

# poetry and python package requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]