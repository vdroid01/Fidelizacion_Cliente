from django.contrib import admin

# Register your models here.
from .models import Cliente

# admin.site.register(Cliente)

#Otra forma de registrar nuestros modelos
@admin.register(Cliente)
class AutoAdmin(admin.ModelAdmin):
    fields = ["Nombre", "Apellido_Paterno", "Apellido_Materno", "genero", "Telefono_Movil", "Direccion", "Correo", "Estado", "Ciudad", "Puntos"]
    list_display = ["Nombre", "Apellido_Paterno", "Puntos"]
# admin.site.register(admin.ModelAdmin)

admin.site.site_header = "Panel de administrador"