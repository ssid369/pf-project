from django.db import models

# Create your models here.
class interest(models.Model):
	image=models.ImageField(upload_to='images/')
	title=models.CharField(max_length=200)
	content=models.TextField()
