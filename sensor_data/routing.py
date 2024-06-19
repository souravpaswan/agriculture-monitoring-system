from django.urls import path
from ..SAMS import consumers

websocket_urlpatterns = [
    path('ws/sensor_data/', consumers.SensorDataConsumer.as_asgi()),
]
