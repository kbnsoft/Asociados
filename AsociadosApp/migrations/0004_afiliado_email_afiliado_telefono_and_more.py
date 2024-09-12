# Generated by Django 5.1.1 on 2024-09-10 21:45

import AsociadosApp.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AsociadosApp', '0003_afiliado_facturado_afiliado_periodo'),
    ]

    operations = [
        migrations.AddField(
            model_name='afiliado',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, validators=[django.core.validators.EmailValidator(message='Introduce una dirección de correo electrónico válida.')]),
        ),
        migrations.AddField(
            model_name='afiliado',
            name='telefono',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='afiliado',
            name='importe',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='afiliado',
            name='periodo',
            field=models.IntegerField(blank=True, null=True, validators=[AsociadosApp.models.validar_periodo]),
        ),
    ]
