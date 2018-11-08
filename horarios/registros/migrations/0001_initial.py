# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-09 18:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ambientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Horarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.IntegerField()),
                ('hora', models.IntegerField()),
                ('minutos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='relacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fila', models.IntegerField()),
                ('columna', models.IntegerField()),
                ('ambientes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registros.Ambientes')),
                ('docentes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registros.Docente')),
                ('horario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registros.Horarios')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registros.Materia')),
            ],
        ),
        migrations.CreateModel(
            name='Semestres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='relacion',
            name='semestre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registros.Semestres'),
        ),
        migrations.AddField(
            model_name='materia',
            name='semestre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registros.Semestres'),
        ),
        migrations.AddField(
            model_name='docente',
            name='materia',
            field=models.ManyToManyField(to='registros.Materia'),
        ),
    ]