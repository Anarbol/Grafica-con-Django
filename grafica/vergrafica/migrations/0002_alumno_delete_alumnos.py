# Generated by Django 4.2 on 2023-04-13 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vergrafica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('hours', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Alumnos',
        ),
    ]
