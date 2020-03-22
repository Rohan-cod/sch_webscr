from django.db import models

# Create your models here.


class Job_posting(models.Model):
	title = models.CharField(max_length=100)
	company = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	url = models.CharField(max_length=600)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title