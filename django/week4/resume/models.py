from django.db import models

# Create your models here.
class Experience(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False)
    location = models.CharField(max_length=64, null=False, blank=False)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title

class Education(models.Model):
    instituition_name = models.CharField(max_length=100,null=False,blank=False)
    location = models.CharField(max_length=100,null=False,blank=False)
    degree = models.CharField(max_length=100,null=False,blank=False)
    major = models.CharField(max_length=100,null=False,blank=False)
    gpa = models.FloatField()

    def __str__(self):
        return self.instituition_name
