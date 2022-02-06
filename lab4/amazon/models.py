from pyexpat import model
from django.db import models
from django.forms import CharField, EmailField

# Create your models here.

class MyUser( models.Model ):
    user_name = models.CharField( max_length=40, primary_key=True )
    password = models.CharField( max_length=100 )

class Student( models.Model ):
    name = models.CharField( max_length=100 )
    age = models.IntegerField()
    notes = models.CharField( null=True, max_length=1000 )
    track_id = models.ForeignKey( 'Track', on_delete=models.CASCADE , null=True, blank=True)
    intake_id = models.ForeignKey( 'Intake', on_delete=models.CASCADE, null=True, blank=True)

class Track( models.Model ):
    name = models.CharField( max_length= 100 )
    description = models.TextField( max_length = 5000 )

class Intake( models.Model ):
    intake_no = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
