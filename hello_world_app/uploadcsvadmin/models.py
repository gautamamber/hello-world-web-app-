from django.db import models

# Create your models here.

class Student(models.Model):
	name = models.CharField(max_length = 20)
	roll_no = models.IntegerField()
	stu_class = models.CharField(max_length = 20)
	school = models.CharField(max_length = 100)
	city = models.CharField(max_length = 20)

	def __str__(self):
		return str(self.name)

	class Meta:
		verbose_name = "student"
		verbose_name_plural = "student"
