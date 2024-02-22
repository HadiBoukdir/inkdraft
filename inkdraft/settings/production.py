from .base import *
import sentry_sdk

DEBUG = False

SECRET_KEY = 'u&e6ehun^13cnms9bp11dcm@p0_6qak53%$ca&36-^t-7gew-4'

ALLOWED_HOSTS = ['localhost', 'inkdraft.co.uk', '*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'inkdraft',
        'USER': 'inkdraft',
        'PASSWORD': 'Testing32145',
        'HOST': 'localhost',
        'PORT': '',
    }
}

sentry_sdk.init(
    dsn="https://bbf5b37efede2eda43d166c440fd201a@o4506792641363968.ingest.sentry.io/4506792644313088",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

try:
    from .local import *
except ImportError:
    pass
