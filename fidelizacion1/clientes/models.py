from django.db import models

# Definir una tupla con los valores del select genero_empleado
generos = (
    ("Masculino", "Masculino"),
    ("Femenino", "Femenino"),
    ("Otro", "Otro"),
)

# Create your models here.
class Cliente(models.Model):
    Nombre = models.CharField(max_length=200)
    Apellido_Paterno = models.CharField(max_length=100)
    Apellido_Materno = models.CharField(max_length=100)
    genero = models.CharField(max_length=80, choices=generos, null=True)
    Telefono_Movil = models.CharField(max_length=10)
    Direccion = models.CharField(max_length=100)
    Correo = models.EmailField(max_length=100)
    Estado = models.CharField(max_length=100)
    Ciudad = models.CharField(max_length=100)  
    Puntos = models.IntegerField()

    class Meta:
        db_table = "Lista de clientes"
        verbose_name = "Cliente" 
        verbose_name_plural = "Clientes"   

    def __str__(self):
        return self.Nombre
    
    @classmethod
    def obtener_todos(cls):
        return cls.objects.all()

        """
        En este ejemplo, se ha añadido un método llamado obtener_todos() 
        que utiliza cls.objects.all() para devolver todos los objetos de la tabla de productos. 
        Ahora, puedes llamar a este método desde cualquier parte de tu código 
        donde tengas acceso al modelo Producto. Por ejemplo:
        """
# from myapp.models import Producto  # Importa tu modelo
# Obtener todos los productos
# productos = Producto.obtener_todos()
        
# Iterar sobre los productos y hacer algo con ellos
# for producto in productos:
# print(producto.nombre, producto.descripcion, producto.precio, producto.fecha_creacion)

# Creamos una clase que permita sumarle puntos a un cliente