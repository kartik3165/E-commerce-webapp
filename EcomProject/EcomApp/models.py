from django.db import models
from django.utils import timezone 
# Create your models here.

class product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    category = models.CharField(max_length=150)
    sub_category = models.CharField(max_length=150)
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    added_time = models.DateTimeField(default=timezone.now , editable=False)
    img = models.ImageField(upload_to='EcomProject\media')
