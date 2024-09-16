# Generated by Django 5.1.1 on 2024-09-13 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AsociadosApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='nombre',
        ),
        migrations.AddField(
            model_name='empresa',
            name='cuit',
            field=models.CharField(default='', max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='nombre_fantasia',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='razon_social',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='rubro',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='tratamiento',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
