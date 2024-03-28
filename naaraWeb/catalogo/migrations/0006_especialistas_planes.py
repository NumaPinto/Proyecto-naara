# Generated by Django 5.0.3 on 2024-03-27 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0005_informacionpagina'),
    ]

    operations = [
        migrations.CreateModel(
            name='Especialistas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_especialista', models.CharField(max_length=100)),
                ('apellido_especialista', models.CharField(max_length=100)),
                ('especialidad_especialista', models.CharField(max_length=100)),
                ('telefono_especialista', models.CharField(max_length=15)),
                ('correo_especialista', models.EmailField(max_length=254)),
                ('foto_especialista', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Planes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_plan', models.CharField(max_length=100)),
                ('descripcion_plan', models.TextField()),
                ('precio_plan', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
