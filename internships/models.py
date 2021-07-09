from django.db import models

# Create your models here.
class intern(models.Model):
	image=models.ImageField(upload_to='images/')
	title=models.CharField(max_length=200)
	startdate=models.DateTimeField(null=True)
	enddate=models.DateTimeField(null=True)
    

