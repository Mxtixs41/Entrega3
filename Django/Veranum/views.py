from django.shortcuts import render, get_object_or_404, redirect
from .models import reserva
from .models import tipo_habitacion
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

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


@login_required
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


@login_required
def crud_view(request):
    listado_reservas = reserva.objects.all()
    return render(request, 'pages/crud.html', {'reserva': listado_reservas})



@login_required
def update_reserva(request, pk):
    instance = get_object_or_404(reserva, pk=pk)
    
    if request.method == 'POST':
        rut = request.POST.get('rut')
        nombre = request.POST.get('nombre')
        appPaterno = request.POST.get('appPaterno')
        appMaterno = request.POST.get('appMaterno')
        habitacion_id = request.POST.get('id_habitacion')
        numero_visitantes = request.POST.get('numVisitantes')
        fecha_entrada = request.POST.get('fechaEntrada')
        fecha_salida = request.POST.get('fechaSalida')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        
        objHabitacion = tipo_habitacion.objects.get(id_habitacion=habitacion_id)
        
        instance.rut = rut
        instance.nombre = nombre
        instance.apellido_paterno = appPaterno
        instance.apellido_materno = appMaterno
        instance.id_habitacion = objHabitacion
        instance.numero_visitantes = numero_visitantes
        instance.fecha_entrada = fecha_entrada
        instance.fecha_salida = fecha_salida
        instance.email = email
        instance.telefono = telefono
        instance.save()
        
        return redirect('crud')  # Redirige a la página del CRUD después de actualizar
    
    tipo = tipo_habitacion.objects.all()
    context = {
        'reserva': instance,
        'habitaciones': tipo,
    }
    return render(request, 'pages/update_reserva.html', context)


def delete_reserva(request, pk):
    instance = get_object_or_404(reserva, pk=pk)
    
    if request.method == 'POST':
        instance.delete()
        return redirect('crud')  # Redirige a la página del CRUD después de eliminar
    
    context = {
        'reserva': instance,
    }
    return render(request, 'pages/delete_reserva.html', context)