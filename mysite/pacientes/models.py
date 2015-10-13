from django.db import models

class Prevision(models.Model):
	nombre=models.CharField(max_length=255,unique=True)
	cobertura=models.IntegerField()

	def __str__(self):
		return self.nombre+"-"+str(self.cobertura)+"%"

class Paciente(models.Model):
	numero_ficha=models.IntegerField(unique=True)
	rut=models.CharField(max_length=30,unique=True)
	nombre=models.CharField(max_length=255)
	apellido_paterno=models.CharField(max_length=255)
	apellido_materno=models.CharField(max_length=255)
	fecha_ingreso=models.DateTimeField('date published')
	prevision=models.ForeignKey(Prevision,null=False)
	#situacion=models.ForeignKey(Situacion)

	def __str__(self):
		return self.rut+" "+self.apellido_paterno+" "+self.apellido_materno+", "+self.nombre+" - "+self.prevision.nombre