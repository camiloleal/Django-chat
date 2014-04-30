from django.db import models

class Usuario(models.Model):
	nombre = models.CharField(max_length=15)
	email = models.EmailField('e-mail', blank=True)
	password = models.CharField(max_length=15)
	estado = models.BooleanField("conectado")

	def __unicode__(self):
		return self.nombre

class Mensaje(models.Model):
	contenido = models.TextField()
	hora = models.TimeField()
	fecha = models.DateTimeField()

	def __unicode__(self):
		return '%s %s' % (self.fecha, self.hora)