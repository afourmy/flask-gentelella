class Config(object):
    SECRET_KEY = 'key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get(
        'GENTELELLA_DATABASE_URL',
        'postgresql://{}:{}@{}:{}/{}'.format(
            environ.get('GENTELELLA_DATABASE_USER', 'gentelella'),
            environ.get('GENTELELLA_DATABASE_PASSWORD', 'gentelella'),
            environ.get('GENTELELLA_DATABASE_HOST', 'localhost'),
            environ.get('GENTELELLA_DATABASE_PORT', 5432),
            environ.get('GENTELELLA_DATABASE_NAME', 'gentelella')
        )
    )


class DebugConfig(Config):
    DEBUG = True
