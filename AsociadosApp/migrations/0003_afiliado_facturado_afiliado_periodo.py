# Generated by Django 5.1.1 on 2024-09-09 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AsociadosApp', '0002_afiliado_created_afiliado_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='afiliado',
            name='facturado',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='afiliado',
            name='periodo',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
