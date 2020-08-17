from django.shortcuts import render

# Create your views here.


def mostrar_inicio(request):    
    
    return render(request, 'index.html')