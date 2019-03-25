from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length = 200)
	description = models.TextField()

	def __str__(self):
		return str(self.title)

	class Meta:
		verbose_name  = "Post"
		verbose_name_plural = "Post"
