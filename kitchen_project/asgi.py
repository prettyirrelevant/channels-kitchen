import os

import django
from channels.auth import AuthMiddlewareStack
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter

import orders.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kitchen_project.settings.development")
django.setup()

application = ProtocolTypeRouter(
    {
        "http": AsgiHandler(),
        "websocket": AuthMiddlewareStack(
            URLRouter(orders.routing.websocket_urlpatterns)
        ),
    }
)
