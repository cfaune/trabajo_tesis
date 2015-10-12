from django.db import models

class Presentacion(models.Model):
	name = models.CharField(max_length=255)
	pub_date = models.DateTimeField('date published')

class Remedio(models.Model):
    name = models.CharField(max_length=255)
    medida = models.IntegerField()
    presentacion = models.ForeignKey(Presentacion)
    pub_date = models.DateTimeField('date published')









# Create your models here.
