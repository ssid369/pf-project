from django.db import models

# Create your models here.
class intern(models.Model):
	image=models.ImageField(upload_to='images/')
	title=models.CharField(max_length=200)
	startdate=models.DateTimeField(null=True)
	enddate=models.DateTimeField(null=True)
	content=models.TextField(null=True)

def __str__(self):
	return self.title

    
def summary(self):
      return self.content[:100]


def stdt(self):
      return self.startdate.strftime('%b %e %Y')


def spdt(self):
      return self.enddate.strftime('%b %e %Y')