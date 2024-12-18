from django.db import models


class VehiculoModel(models.Model):
    MARCAS_CHOICES = [
        ('Fiat', 'Fiat'),
        ('Chevrolet', 'Chevrolet'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota'),
    ]

    CATEGORIAS_CHOICES = [
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga'),
    ]

    marca = models.CharField(
        max_length=20,
        choices=MARCAS_CHOICES,
        default='Ford'
    )
    
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50, unique=True)
    serial_motor = models.CharField(max_length=50, unique=True)
    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIAS_CHOICES,
        default='Particular'
    )
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.marca} - {self.modelo}"

