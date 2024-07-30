from django.db import models

# Create your models here.
class Interview(models.Model):
    company = models.CharField(max_length=70)
    hr = models.CharField(max_length=70)
    phone = models.CharField(max_length=12)
    time = models.DateTimeField()
    status = models.BooleanField()
    comment = models.TextField()
