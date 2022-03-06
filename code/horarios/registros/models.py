from django.db import models
from django.contrib import admin
# Create your models here.
class Horarios(models.Model):
	dia=models.IntegerField()
	hora=models.IntegerField()
	minutos=models.IntegerField()
	def __unicode__(self):
		dias=["lunes","martes","miercoles","jueves","viernes"]
		return "%s: %s:%s"%(dias[self.dia],self.hora,self.minutos)
class Ambientes(models.Model):
	nombre=models.CharField(max_length=20)
	cantidades=models.IntegerField(default=0)
	def __unicode__(self):
		return "%s"%(self.nombre)
class Semestres(models.Model):
	nombre=models.CharField(max_length=50)
	def __unicode__(self):
		return "%s"%(self.nombre)
class Materia(models.Model):
	sigla=models.CharField(max_length=50)
	nombre=models.CharField(max_length=50)
	semestre=models.ForeignKey(Semestres)
	def __unicode__(self):
		return "%s"%(self.sigla)
class Docente(models.Model):
	nombre=models.CharField(max_length=50)
	apellido=models.CharField(max_length=50)
	materia=models.ManyToManyField(Materia)
	def __unicode__(self):
		return "%s %s"%(self.nombre,self.apellido)
class relacion(models.Model):
	horario=models.ForeignKey(Horarios)
	ambientes=models.ForeignKey(Ambientes)
	docentes=models.ForeignKey(Docente)
	materia=models.ForeignKey(Materia)
	semestre=models.ForeignKey(Semestres)
	fila=models.IntegerField()
	columna=models.IntegerField()
	def __unicode__(self):
		return "%s %s %s %s"%(self.horario,self.ambientes,self.docentes,self.materia)