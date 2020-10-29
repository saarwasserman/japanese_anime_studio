import os


basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:

    GHIBLI_BASE_URL = "https://ghibliapi.herokuapp.com"
    REDIS_URL = "localhost"  # "redis"  # for docker-compose
    MOVIES_UPDATE_INTERVAL = 60  # in seconds
    MOVIES_USE_CRON = False


class DevelopmentConfig(BaseConfig):
    REDIS_URL = "localhost"
    MOVIES_UPDATE_INTERVAL = 10
    DEBUG = True


class DockerConfig(BaseConfig):
    REDIS_URL = "redis"
    MOVIES_UPDATE_INTERVAL = 10
    DEBUG = True


class ProductionConfig(BaseConfig):
    REDIS_URL = "redis"
    DEBUG = False


config = {
    "development": DevelopmentConfig,
    "docker": DockerConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}
