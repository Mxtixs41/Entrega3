from django.db import models


# Create your models here.
class tipo_habitacion(models.Model):
    id_habitacion = models.AutoField(primary_key=True, db_column="idHabitacion")
    habitacion = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return str(self.habitacion)


class reserva(models.Model):
    
    rut= models.CharField(primary_key=True,max_length=10)
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    id_habitacion = models.ForeignKey(
        "tipo_habitacion",on_delete=models.CASCADE, db_column="IDHABITACION"
    )
    numero_visitantes = models.PositiveIntegerField()
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    email = models.EmailField(max_length=100, unique=True, blank=True , null=True)
    telefono = models.CharField(max_length=12)
    total = models.CharField(max_length=8)


    def __str__(self):
       return(
           str(self.nombre)
           + " "
           + str(self.apellido_paterno)
           
           )

