from django.db import models

# Create your models here.
class Bank(models.Model):
    b_name = models.CharField(max_length=50)
    b_rate = models.IntegerField(default=0)
    
    def __str__(self):
        return self.b_name