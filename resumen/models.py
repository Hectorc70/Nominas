from django.db import models

# Create your models here.


class Nomina(models.Model): 
    nombre  = models.CharField(max_length=20, verbose_name="NOMBRE_NOMINA")
    anno  = models.CharField(max_length=4,verbose_name="ANNO")
    periodo  = models.CharField(max_length=2,verbose_name="PERIODO")
    id_ejecucion  = models.CharField(max_length=20, verbose_name="ID_EJECUCION")
    fecha_pago = models.CharField(max_length=10, verbose_name="FECHA_PAGO")   
    num_xml = models.IntegerField(verbose_name="NUM_XML")
    importe_isr  = models.FloatField(verbose_name="IMPORTE_ISR")
    isr_retim  = models.FloatField(verbose_name="ISR_TIM")   
    comentario  = models.CharField(max_length=300, verbose_name="COMENTARIO")
    mod_usuario  = models.CharField(max_length=8, verbose_name="MOD_USUARIO")
    fecha_mod  = models.DateTimeField(verbose_name="FECHA_MODIFICACION", auto_now=True)
    
    class Meta:
        db_table = 'Nominas'
    def __str__(self):

        return """Nomina: %s  
                id de Nomina: %s  
                XMLS´S: %s  
                ISR: %s"""%(self.nombre, self.id_ejecucion,
                                        self.num_xml, self.importe_isr)


