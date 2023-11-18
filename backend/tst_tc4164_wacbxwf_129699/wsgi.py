"""
WSGI config for tst_tc4164_wacbxwf_129699 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "tst_tc4164_wacbxwf_129699.settings"
)

application = get_wsgi_application()
