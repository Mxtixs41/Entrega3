from django.shortcuts import render, get_object_or_404, redirect
from .models import reserva
from .models import tipo_habitacion
# Create your views here.

def index(request):
    context={
        "usuario":"nico"
    }
    return render(request, 'pages/index.html', context)

def login_view(request):
    return render(request, 'pages/login.html')

def actividades_view(request):
    return render(request, 'pages/actividades.html')

def restaurante_view(request):
    return render(request, 'pages/restaurante.html')



def panel_view(request):
    return render(request, 'pages/panel.html')



def habitaciones_view(request):
    if request.method != "POST":
        tipo = tipo_habitacion.objects.all()
        context = {
            "habitaciones" : tipo,
        }
        return render(request, "pages/habitaciones.html", context )
    else:
        rut= request.POST["rut"]
        nombre = request.POST["nombre"]
        appPaterno = request.POST["appPaterno"]
        appMaterno = request.POST["appMaterno"]
        habitacion = request.POST['id_habitacion']
        numero_visitantes = request.POST["numVisitantes"]
        fecha_entrada = request.POST["fechaEntrada"]
        fecha_salida = request.POST["fechaSalida"]
        email = request.POST["email"]
        telefono = request.POST["telefono"]


        objHabitacion = tipo_habitacion.objects.get(id_habitacion= habitacion)

        obj = reserva.objects.create(
            rut=rut,
            nombre=nombre,
            apellido_paterno = appPaterno,
            apellido_materno = appMaterno,
            id_habitacion = objHabitacion,
            numero_visitantes = numero_visitantes,
            fecha_entrada = fecha_entrada,
            fecha_salida = fecha_salida,
            email = email,
            telefono = telefono
        )
        obj.save()

        
        tipo = tipo_habitacion.objects.all()
        context = {
            "mensaje" : "Registro Exitoso",
            "habitaciones":tipo
        }

        return render(request, "pages/habitaciones.html", context)


def carrito_view(request):
    ultima_reserva = reserva.objects.latest('fecha_entrada')
    return render(request, 'pages/carrito.html', {'reserva': ultima_reserva})


def crud_view(request):
    listado_reservas = reserva.objects.all()
    return render(request, 'pages/crud.html', {'reserva': listado_reservas})