from django.urls import path
from .views import servicios_mudanzas

urlpatterns = [
    path('servicios/', servicios_mudanzas, name='servicios_mudanzas'),
]