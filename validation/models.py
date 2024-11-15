from django.db import models

# Create your models here.

class Admission(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=200, null=False)
    image = models.ImageField(upload_to='validation', null=True, blank=True)
    
    def __str__(self):
        return self.name