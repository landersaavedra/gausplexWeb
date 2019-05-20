import os

__STATIC_PATH = os.path.dirname(os.path.dirname(__file__))


STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(__STATIC_PATH, "../gausplexWeb/static"),
    #os.path.join(__STATIC_PATH, "../gausplexWeb/apps/security/static"),
)

STATIC_ROOT = os.path.join(__STATIC_PATH, '../static/')
