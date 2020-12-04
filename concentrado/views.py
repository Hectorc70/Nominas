from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.db.models import Q

from resumen.models import Nomina

from concentrado.recalculo import ArchivoRecalculo
from concentrado.models import Recalculo
from concentrado.modulos.rutas import abrir_archivo
# Create your views here.
@login_required()
def mostrar_concentrado(request):
    
    ultimo_per = Nomina.objects.latest('anno', 'periodo')    #ultimo periodo del ultmo año
    periodo2 = int(ultimo_per.periodo)-1 
    nominas = Nomina.objects.filter(Q(anno=ultimo_per.anno,         #registros con el año y periodo pasados
    periodo=ultimo_per.periodo) | Q(periodo=periodo2))
    
    ultimo_per_rec = Recalculo.objects.latest('anno', 'periodo')
    periodo2_rec = int(ultimo_per_rec.periodo)-1 
    registros_recalculo = Recalculo.objects.filter(Q(anno=ultimo_per.anno,         #registros con el año y periodo pasados
    periodo=ultimo_per_rec.periodo) | Q(periodo=periodo2_rec))

    """  for registro in registros_recalculo:
        breakpoint();
        print(registro) """
    datos_para_mostrar = {'timbrado':nominas,  'recalculo':''}
    
    return render(request, 'concentrado.html', {'datos': datos_para_mostrar})


def cargar_archivo(request):
    ruta = abrir_archivo()
    if ruta != '': 
        datos = ArchivoRecalculo(ruta)
        datos_recalculo = datos.ejecutar()
        breakpoint();
        if datos_recalculo:            
            for hoja, datos in datos_recalculo.items():   
                for dato in datos:
                    periodo  = dato[0]
                    anno = dato[1]
                    control  = dato[2]
                    importe  = dato[3]
                    importe_redondeado  = dato[4]
                    registro = Recalculo(periodo=periodo, anno=anno,control=control,
                                        imp_recalc=importe, imp_recalc_red=importe_redondeado,
                                        tipo_nom=hoja)

                    registro.save()

            messages.success(request, 'Datos guardados en la Base de datos')
            return redirect('concentrado')


    else:        
        messages.error(request, 'Se debe seleccionar un archivo')
        return redirect('concentrado')
        

