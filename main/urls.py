from django.urls import path
from .views import servicios_mudanzas

urlpatterns = [
    path('', servicios_mudanzas, name='servicios_mudanzas'),
]