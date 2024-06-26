from django.shortcuts import render
from premios.models import Premio

def premios_view(request):
    # Obtener la suma de los registros del modelo Premio
    suma_premios = Premio.objects.count()

    # Obtener todos los registros del modelo Premio
    premios = Premio.objects.all()

    # Crear una lista de diccionarios con la información de cada premio
    lista_premios = []
    for premio in premios:
        premio_info = {
            'titulo': premio.Nombre_Premio,
            'descripcion': premio.Descripcion,
            'imagen_url': premio.Imagen.url if premio.Imagen else '',  # Suponiendo que imagen es un campo FileField
        }
        lista_premios.append(premio_info)

    # Pasar los datos como contexto al template
    context = {
        'suma_premios': suma_premios,
        'premios': lista_premios,
    }

    # Renderizar el template con el contexto
    return render(request, 'prueba.html', context)