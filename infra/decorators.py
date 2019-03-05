import logging
import logging.config
from functools import wraps

LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'padrao': {
            'class': 'logging.Formatter',
            'format': '{levelname} {created} {msg}',
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


def log_request(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        response = func(request, *args, **kwargs)
        usuario = request.user.username if request.user.is_authenticated else 'anonimo'
        msg = f'{usuario} - {request.path} - {request.method} - {response.status_code}'
        logger.info(msg)
        return response

    return wrapper
