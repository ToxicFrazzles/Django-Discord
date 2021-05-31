# This file sets up and configures Django. It's used by scripts need to execute as if running in a Django server.
from pathlib import Path
import django
from django.conf import settings


BASE_DIR = Path(__file__).parent / "django_discord"


def boot_django():
    settings.configure(
        BASE_DIR=BASE_DIR,
        DEBUG=True,
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": BASE_DIR/"db.sqlite3"
            }
        },
        INSTALLED_APPS=(
            "django_discord",
        ),
        TIME_ZONE="GMT",
        USE_TZ=True,
    )
    django.setup()
