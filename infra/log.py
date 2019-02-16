import logging
import logging.config
from functools import wraps

LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'padrao': {
            'class': 'logging.Formatter',
            'format': '{levelname} {module} {created} {msg}',
            'style': '{',
        },
    },
    'handlers': {
        'arquivo': {
            'class': 'logging.FileHandler',
            'level': 'INFO',
            'formatter': 'padrao',
            'filename': 'logs.log',
        },
    },
    'loggers': {
        'django': {},
        'django.server': {},
        'mail_admins': {},
        'promisoria': {
            'handlers': ['arquivo'],
            'level': 'INFO',
        },
    },
}

logging.config.dictConfig(LOGGING_CONFIG)

logger = logging.getLogger('promisoria')


def log(mensagem=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            logger.info(mensagem)
            return result

        return wrapper

    return decorator
