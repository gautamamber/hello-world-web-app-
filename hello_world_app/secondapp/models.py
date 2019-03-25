from django.db import models

# Create your models here.

class City(models.Model):
	name = models.CharField(max_length = 10)
	zipcode = models.IntegerField()

	def __str__(self):
		return str(self.name)

	class Meta:
		verbose_name = "City"
		verbose_name_plural = "City"

