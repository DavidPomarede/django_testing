import sys
import os

from django.core.wsgi import get_wsgi_application

app_path = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), os.pardir, os.pardir))
sys.path.append(app_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_config.prod")
application = get_wsgi_application()
