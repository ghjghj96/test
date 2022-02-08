from django.db import models

# Create your models here.
class Student(models.Model):
    s_name = models.CharField(max_length=50)
    s_major = models.CharField(max_length=50)
    s_age = models.IntegerField(default=20)
    s_grade = models.IntegerField(default=1)
    s_gender = models.CharField(max_length=50)
    
    def __str__(self):
        return self.s_name