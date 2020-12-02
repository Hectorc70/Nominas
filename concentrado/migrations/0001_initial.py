# Generated by Django 3.0.2 on 2020-12-02 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recalculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(max_length=2, verbose_name='Periodo')),
                ('anno', models.CharField(max_length=4, verbose_name='Año')),
                ('control', models.CharField(max_length=8, verbose_name='Num Control')),
                ('imp_recalc', models.FloatField(verbose_name='Recalculo')),
                ('imp_recalc_red', models.FloatField(verbose_name='Recalculo Redondeado')),
                ('tipo_nom', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'Recalculo',
            },
        ),
    ]