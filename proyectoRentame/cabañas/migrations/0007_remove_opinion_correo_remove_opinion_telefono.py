# Generated by Django 4.0.5 on 2022-08-28 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cabañas', '0006_alter_opinion_options_opinion_imagenop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opinion',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='opinion',
            name='telefono',
        ),
    ]
