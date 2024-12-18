from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import VehiculoModel
from .forms import VehiculoForm
from django.views.generic import TemplateView, ListView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import Permission

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Asignar el permiso 'visualizar_catalogo' al usuario
            permission = Permission.objects.get(codename='visualizar_catalogo')
            user.user_permissions.add(permission)
            login(request, user)
            return redirect('vehiculo:list')  # Redirigir a la lista de vehículos
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def index(request):
    return render(request, 'index.html')

def add_vehiculo(request):
    return render(request, 'add.html')

def list_vehiculo(request):
    if request.user.is_authenticated:  # Verificar si el usuario está logueado
        vehiculos = VehiculoModel.objects.all()
        return render(request, 'list.html', {'vehiculos': vehiculos})
    else:
        mensaje = "Debes iniciar sesión para ver la lista de vehículos."
        return render(request, 'list.html', {'mensaje': mensaje})

def add_vehiculo(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = VehiculoForm(request.POST)
            if form.is_valid():
                form.save()
                # Redirigir al listado de vehículos después de guardar el nuevo vehículo
                return redirect('list')  # 'list' debe ser el nombre de la vista para listar los vehículos
        else:
            form = VehiculoForm()
        return render(request, 'add.html', {'form': form})
    else:
        mensaje = "Debes estar autenticado para agregar vehículos."
        return render(request, 'add.html', {'mensaje': mensaje})
def new_vehiculo_view(request):
    context ={}
    # crear el objeto form
    form = VehiculoForm(request.POST or None, request.FILES or None)
    # verificar si el formulario es valido
    if form.is_valid():
        # guardar los datos del formulario al modelo
        form.save()
        return redirect('/')
    context = {'formulariovehiculo' : form}
    return render(request, "formulario.html", context)
from django.shortcuts import render
from .models import VehiculoModel


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list')  # Redirigir a la página de listado después de iniciar sesión
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})

def logout_view(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('index') 

class VehiculoListView(ListView):
    template_name = 'formulario.html'
    model= VehiculoModel
    context_object_name = 'formulario_vehiculo'