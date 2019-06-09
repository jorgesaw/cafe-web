# Generated by Django 2.2.1 on 2019-05-31 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter a title', max_length=210, verbose_name='Título')),
                ('content', models.TextField(help_text='Enter a content', verbose_name='Contenido')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Última actualización')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
            ],
            options={
                'verbose_name': 'pagina',
                'verbose_name_plural': 'paginas',
                'ordering': ['title'],
            },
        ),
    ]