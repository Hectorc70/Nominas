from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, permission_required

from django.contrib.auth.models import User
from usuarios.models import Usuario
from resumen.forms import RegistroForm, RegistroNomina
from resumen.models import Nomina
from django.contrib.auth import REDIRECT_FIELD_NAME
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
        
        usuario_r = Usuario.objects.create_user(control=control, password=password, 
                                                first_name=name, last_name=last_name,
                                                second_last_name=last_second_name,
                                                email=email)
        if usuario_r:
            login(request, usuario_r)
            messages.success(request, 'Usuario creado correctamente')

            return redirect('index')

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
            return redirect('index')
            
        
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            return render(request, 'login.html')

    return render(request, 'login.html')

@login_required()
def mostrar_inicio(request):    
    nominas = Nomina.objects.all()
    return render(request, 'index.html', {'nominas':nominas})
    
@login_required()
def salir(request):
    logout(request)
    messages.success(request, "Sesion Finalizada")

    return redirect('login')

@login_required()
def registro_nomina(request):
    usuario_l= request.user.control        
    formulario = RegistroNomina(request.POST)
    if request.method == 'POST' and formulario.is_valid():
        nombre = formulario.cleaned_data.get('nombre')
        anno = formulario.cleaned_data.get('anno')
        periodo = formulario.cleaned_data.get('periodo')
        id_ejecucion = formulario.cleaned_data.get('id_ejecucion')
        fecha_pago = formulario.cleaned_data.get('fecha_pago')
        num_xml = formulario.cleaned_data.get('num_xml')
        importe_isr = formulario.cleaned_data.get('importe_isr')
        isr_retim = formulario.cleaned_data.get('isr_retim')
        comentario = formulario.cleaned_data.get('comentario')          

        nom = Nomina(nombre=nombre, anno=anno, periodo=periodo,
                    id_ejecucion=id_ejecucion, fecha_pago=fecha_pago,
                    num_xml=num_xml, importe_isr=importe_isr,
                    isr_retim=isr_retim, comentario=comentario,
                    mod_usuario=usuario_l)
        nom.save()

        messages.success(request, 'Registro Guardado')

        return redirect('index')

    else:
        messages.error(request, 'Registro No Guardado')

    return render(request, 'form_nomina.html', {'form': formulario,'usuario': usuario_l})