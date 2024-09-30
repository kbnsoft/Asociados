from django.db import models

class Localidad(models.Model):
	descripcion = models.CharField(max_length=50)
	departamento = models.ForeignKey('Departamento', on_delete=models.CASCADE, blank=True, null=True)
	provincia = models.ForeignKey('Provincia', on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return self.descripcion

		
class Departamento(models.Model):
	codigo = models.IntegerField()
	descripcion = models.CharField(max_length=50)
	provincia = models.ForeignKey('Provincia', on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return self.descripcion

class Provincia(models.Model):
	codigo = models.CharField(max_length=1)
	descripcion = models.CharField(max_length=50)

	def __str__(self):
		sc = str(self.codigo) + ' - ' + self.descripcion
		return sc
