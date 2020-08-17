from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext

from django.contrib.auth.models import User
from usuarios.models import Usuario
from resumen.forms import RegistroForm
from resumen.models import Nomina
# Create your views here.
def verifica_cookie(request):
    if request.session.test_cookie_worked():
        request.session.delate_test_cookie()
    
    else:
        request.session.set_test_cookie()
        messages.error(request, 'Porfavor habilite las cookies')

    return render(request, 'login.html') 
    
def registro_usuario(request):
    formulario = RegistroForm(request.POST or None)

    if request.method == 'POST' and formulario.is_valid():
        control = formulario.cleaned_data.get('control')
        name = formulario.cleaned_data.get('name')
        last_name = formulario.cleaned_data.get('last_name')
        last_second_name = formulario.cleaned_data.get('last_second_name')
        email = formulario.cleaned_data.get('email')
        password = formulario.cleaned_data.get('password')
        
        usuario = Empleado.objects.create_user(control=control, password=password, 
                                                first_name=name, last_name=last_name,
                                                second_last_name=last_second_name,
                                                email=email)
        if usuario:
            login(request, usuario)
            messages.success(request, 'Usuario creado correctamente')

            return render(request, 'index.html', {'control':control})

    return render(request, 'register.html', {'form': formulario})

@csrf_protect
def ingresar(request):  
    """vista para poder ingresar a la pagina""" 

    if request.method == 'POST': 
        control = request.POST.get('control')
        psword  = request.POST.get('psword')
        
        #control = '317484'
        #psword  = '121212'        
        
        usuario = authenticate(control = control, password = psword)
        if usuario:
            login(request, usuario)

            messages.success(request, 'A ingresado correctamente %s'%(usuario.control))
            return HttpResponse('index', usuario)
            
        
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            return render(request, 'login.html')

    return render(request, 'login.html')
def mostrar_inicio(request):    
    nominas = Nomina.objects.all()
    return render(request, 'index.html', {'nominas':nominas})
    return render(request, 'index.html')