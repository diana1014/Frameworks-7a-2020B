# Generated by Django 3.1.1 on 2020-10-30 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Afiliados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('id_ciudad', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('fecha_creacion', models.CharField(max_length=100)),
                ('fecha_modificacion', models.CharField(max_length=100)),
            ],
        ),
    ]
