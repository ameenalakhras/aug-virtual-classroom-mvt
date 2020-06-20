
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'virtual_class.settings')

application = get_wsgi_application()
