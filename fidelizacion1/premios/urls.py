from django.urls import path
from .views import premios_view  # Importa la vista que hemos definido

urlpatterns = [
    path('', premios_view, name='obtener_premios'),
    # Otros paths de tu aplicación
]