import os

BASE_DIR = os.path.dirname(__file__)

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.sessions",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.admin",
    "django_tables2",
    "django_tables2_bulma_template",
)

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# MIDDLEWARE_CLASSES = (
#     "django.middleware.common.CommonMiddleware",
#     "django.middleware.csrf.CsrfViewMiddleware",
# )

ROOT_URLCONF = "tests.urls"
SECRET_KEY = "secretkey"
SITE_ROOT = os.path.dirname(os.path.abspath(__file__))


TEMPLATE_DEBUG = True
TEMPLATE_DIRS = (os.path.join(BASE_DIR, "templates"),)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": TEMPLATE_DIRS,
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ],
            "debug": TEMPLATE_DEBUG,
        },
    },
]

# Set to a default non-existing value here, and change per Table to avoid false positive in tests
DJANGO_TABLES2_TEMPLATE = "NOTVALID"