import logging
import logging.config


def setup_logging(verbose: bool = False):
    """
    setup logging config by updating the arq logging config
    """
    log_level = 'DEBUG' if verbose else 'INFO'
    # raven_dsn = os.getenv('RAVEN_DSN', None)
    # if raven_dsn in ('', '-'):
    #     # this means setting an environment variable of "-" means no raven
    #     raven_dsn = None
    config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {'df': {'format': '%(levelname)s %(name)s %(message)s'}},
        'handlers': {
            'df': {'level': log_level, 'class': 'logging.StreamHandler', 'formatter': 'df'},
            # 'sentry': {
            #     'level': 'WARNING',
            #     'class': 'raven.handlers.logging.SentryHandler',
            #     'dsn': raven_dsn,
            #     'release': os.getenv('COMMIT', None),
            #     'name': os.getenv('SERVER_NAME', '-'),
            # },
        },
        'loggers': {
            'df': {'handlers': ['df'], 'level': log_level},  # Add sentry as handler when adding Sentry
            # 'gunicorn.error': {'handlers': ['sentry'], 'level': 'ERROR'},
        },
    }
    logging.config.dictConfig(config)
