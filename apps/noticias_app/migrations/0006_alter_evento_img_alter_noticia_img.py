# Generated by Django 4.0.6 on 2022-09-01 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias_app', '0005_alter_comentarios_cuerpo_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='img',
            field=models.ImageField(blank=True, help_text='Seleccione una imagen para mostrar.', null=True, upload_to='static/img/eventos'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='img',
            field=models.ImageField(blank=True, help_text='Seleccione una imagen para mostrar.', null=True, upload_to='static/img/noticias'),
        ),
    ]
