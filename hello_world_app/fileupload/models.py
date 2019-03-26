from django.db import models

# Create your models here.

class FileUpload(models.Model):
	file = models.FileField(blank = False, null = False)
	text = models.CharField(max_length = 200)

	def __str__(self):
		return str(self.text)

	class Meta:
		verbose_name = "File Upload"
		verbose_name_plural = "File Upload"
