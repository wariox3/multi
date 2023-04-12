# Generated by Django 4.2 on 2023-04-12 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_empresa_fkm', models.IntegerField(null=True)),
                ('codigo_identificacion_fkm', models.IntegerField(null=True)),
                ('numero_identificacion', models.CharField(max_length=3)),
                ('digito_verificacion', models.CharField(max_length=1)),
                ('nombre_corto', models.CharField(max_length=200)),
                ('nombre1', models.CharField(max_length=50)),
                ('nombre2', models.CharField(max_length=50)),
                ('apellido1', models.CharField(max_length=50)),
                ('apellido2', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('codigo_ciudad_fkm', models.IntegerField()),
                ('codigo_postal', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=50)),
                ('celular', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=200)),
                ('codigo_tipo_persona_fkm', models.IntegerField(null=True)),
                ('codigo_regimen_fkm', models.IntegerField(null=True)),
                ('codigo_cuenta_cobrar_fk', models.IntegerField(null=True)),
                ('codigo_cuenta_pagar_fk', models.IntegerField(null=True)),
            ],
        ),
    ]
