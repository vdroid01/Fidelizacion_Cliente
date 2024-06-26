from django.urls import path, include
from rest_framework.routers import DefaultRouter
from clientes.views import IndexView, ClienteView, MyModelViewSet

router = DefaultRouter()
router.register(r'Cliente', MyModelViewSet)


urlpatterns = [
    path('prueba', IndexView),
    path('', include(router.urls)),
    path('cliente/', ClienteView),
]
