from django.db import models

# Create your models here.


class Recalculo(models.Model):
    periodo = models.CharField(max_length=2, verbose_name="Periodo")
    anno = models.CharField(max_length=4, verbose_name="Año", blank=False)
    control = models.CharField(max_length=8, verbose_name="Num Control")
    imp_recalc = models.FloatField(verbose_name="Recalculo")
    imp_recalc_red = models.FloatField(verbose_name="Recalculo Redondeado")
    tipo_nom = models.CharField(max_length=40)


    class Meta:
        db_table = 'Recalculo'

    def __str__(self):

        return """Tipo Nomina: %s  
                Periodo: %s  
                Recalculo: %s"""%(self.tipo_nom, self.periodo,
                                    self.imp_recalc)


