from django.db import models

# Create your models here.

class Student(models.Model):
	name = models.CharField(max_length = 20)
	roll_no = models.IntegerField(blank = True, null = True)
	stu_class = models.CharField(max_length = 20, blank = True, null = True)
	school = models.CharField(max_length = 100, blank = True, null = True)
	city = models.CharField(max_length = 20, blank = True, null = True)

	def __str__(self):
		return str(self.name)

	class Meta:
		verbose_name = "student"
		verbose_name_plural = "student"
