# Generated by Django 3.0.2 on 2020-08-20 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nomina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, verbose_name='NOMBRE_NOMINA')),
                ('anno', models.CharField(max_length=4, verbose_name='ANNO')),
                ('periodo', models.CharField(max_length=2, verbose_name='PERIODO')),
                ('id_ejecucion', models.CharField(max_length=20, verbose_name='ID_EJECUCION')),
                ('fecha_pago', models.CharField(max_length=10, verbose_name='FECHA_PAGO')),
                ('num_xml', models.IntegerField(verbose_name='NUM_XML')),
                ('importe_isr', models.FloatField(verbose_name='IMPORTE_ISR')),
                ('isr_retim', models.FloatField(verbose_name='ISR_TIM')),
                ('comentario', models.CharField(max_length=300, verbose_name='COMENTARIO')),
                ('mod_usuario', models.CharField(max_length=8, verbose_name='MOD_USUARIO')),
                ('fecha_mod', models.DateTimeField(auto_now=True, verbose_name='FECHA_MODIFICACION')),
            ],
            options={
                'db_table': 'Nominas',
            },
        ),
    ]
