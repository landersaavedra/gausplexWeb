BEFORE_DJANGO_APPS = (

)

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.humanize',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'web.apps.WebConfig',
)

LOCAL_APPS = (
    #'gausplexWeb.apps.flow',
    'gausplexWeb.apps.web',
    #'gausplexWeb.apps.security',
)

THIRD_PARTY_APPS = (
    'solo',
)


INSTALLED_APPS = BEFORE_DJANGO_APPS + DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS
