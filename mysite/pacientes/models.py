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

class Situacion(models.Model):
	nombre=models.CharField(max_length=255,unique=True)

	def __str__(self):
		return self.nombre

class Diagnostico(models.Model):
	paciente=models.ForeignKey(Paciente,null=False)
	nombre=models.CharField(max_length=255,unique=True)
	descripcion=models.CharField(max_length=255,unique=True)
	situacion=models.ForeignKey(Situacion,null=False)
	fecha_diagnostico=models.DateTimeField('date published')

	def __str__(self):
		return self.paciente.apellido_paterno+" "+self.paciente.apellido_materno+", "+self.paciente.nombre+" "+self.nombre+" "+self.situacion.nombre