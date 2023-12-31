# Generated by Django 4.2.7 on 2023-11-21 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aeropuerto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(max_length=3, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('foto_aeropuerto', models.ImageField(upload_to='foto_aeropuerto/')),
            ],
        ),
        migrations.CreateModel(
            name='Vuelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_vuelo', models.IntegerField(max_length=5, unique=True)),
                ('origen', models.CharField(max_length=100)),
                ('destino', models.CharField(max_length=100)),
                ('cod_aeropuerto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionPasajeros.aeropuerto')),
            ],
        ),
        migrations.CreateModel(
            name='Pasajero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_pasajero', models.IntegerField()),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('celular', models.IntegerField()),
                ('correo', models.CharField(max_length=100)),
                ('num_vuelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionPasajeros.vuelo')),
            ],
        ),
    ]
