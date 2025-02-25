# Generated by Django 5.1.3 on 2024-11-29 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
