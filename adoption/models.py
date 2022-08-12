from re import T
from django.db import models

class Pet(models.Model):
    sex_choices = [('M',"Male"),('F','Female')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30,blank=True)
    description = models.TextField()
    sex = models.CharField(max_length=1 ,choices=sex_choices,blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)
    vaccination = models.ManyToManyField('Vaccine',blank=True)

    def __str__(self) -> str:
        return self.name

class Vaccine(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.name

    
