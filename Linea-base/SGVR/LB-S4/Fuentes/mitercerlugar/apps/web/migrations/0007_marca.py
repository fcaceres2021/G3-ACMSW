# Generated by Django 3.0.7 on 2020-07-14 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_evento_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('estado', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
