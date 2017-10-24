import os
from channels import asgi 


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_ig.settings")
channel_layer = asgi.get_channel_layer()
