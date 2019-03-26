from django.db import models

# Create your models here.

class Person(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField(blank=True)
	birth_date = models.DateField()
	location = models.CharField(max_length=100, blank=True)

	def __str__ (self):
		return str(self.name)

	class Meta:
		verbose_name = "Person"
		verbose_name_plural = "Person"
