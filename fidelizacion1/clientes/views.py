from rest_framework import viewsets

from django.shortcuts import render
from .models import Cliente
from .serializers import ClienteSerializer

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    
# Create your views here.
def IndexView(request):
    return render(request, "index.html")

def ClienteView(request):
    #Obtener todos los clientes desde la base de datos
    clientes = Cliente.objects.all()

    #Pasar los clientes a la plantilla como texto
    return render(request, 'clientes.html', {'clientes':clientes})
