from django.urls import path
from principal.views import PrincipalView

urlpatterns = [
    path('', PrincipalView),
]
