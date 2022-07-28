from secrets import choice
from django.db import models
from django.forms import CharField, DateField, FloatField, NumberInput, TextInput
from django.urls import clear_script_prefix

class Patient(models.Model):
    patient_number=models.CharField(max_length=15,null=True,unique=True)
    registration_date=models.DateField()
    first_name=models.CharField(max_length=17,null=True)
    last_name=models.CharField(max_length=20,null=True)
    date_of_birth=models.DateTimeField()
    gender_choice=(
        ("male","Male"),
        ("female","Female"),
        ("other","Other"),
    )
    gender=models.CharField(max_length=17,choices=gender_choice,null=True)
    

class Vital(models.Model):
    patient_name=models.CharField(max_length=15)
    patient_visit_date=models.FloatField()
    patient_height_in_center_metres=models.FloatField()
    patient_weight_in_kg=models.FloatField()
    patient_Bmi=models.FloatField()
    
    @property
    def bmi(self):
        height = self.patient_height_in_center_metres/100
        bmi=self.patient_weight_in_kg/(height*height)
        return bmi


class DietChoices(models.TextChoices):
    YES="Yes",
    NO="No"
    
class Visit(models.Model):
    patient_name=models.CharField(max_length=25)
    visit_date=models.DateField()
    general_health_choice=(
        ("good","Good"),
        ("poor","Poor"),
 
    )
    general_health=models.CharField(max_length=17,choices=general_health_choice,null=True)
    comments=models.CharField(max_length=500,null=True)
    weight_choice = models.CharField(max_length=17,choices=DietChoices.choices, default=DietChoices.NO)
   
  
    