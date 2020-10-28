import os


basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:

    GHIBLI_BASE_URL = "https://ghibliapi.herokuapp.com"
    REDIS_URL = "redis://localhost"
    CRON_MOVIES_USE = False


# class DevelopmentConfig(BaseConfig):
#     DEBUG = True


# class StagingConfig(BaseConfig):
#     DEBUG = True


# class ProductionConfig(BaseConfig):





config = {
    # 'development': DevelopmentConfig,
    # 'staging': TestingConfig,
    # 'production': ProductionConfig,
    # 'heroku': HerokuConfig,
    # 'docker': DockerConfig,

    'default': BaseConfig
}