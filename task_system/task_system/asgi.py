"""
ASGI config for task_system project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_system.settings')

application = get_asgi_application()

from channels.routing import ProtocolTypeRouter,URLRouter
from django.urls import path
from task.consumers import MyConsumer

ws_pattern=[
    path('ws/main',MyConsumer)
]

application = ProtocolTypeRouter({
    # WebSocket chat handler
    "websocket":(
            URLRouter(ws_pattern)
    ),
})
        