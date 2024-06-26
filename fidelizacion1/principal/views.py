from django.shortcuts import render

from clientes.models import Cliente
# Create your views here.

def PrincipalView(request):
    clientes = Cliente.objects.filter(Nombre='Santos')

    return render(request, 'iniciousua.html', {'clientes':clientes})
