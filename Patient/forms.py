
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from bootstrap_datepicker_plus.widgets import DatePickerInput

from .models import Patient, Visit, Vital,DietChoices

class PatientRegistrationForms(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"
        widgets = {
            'patient_number': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:99%'}),
            'regstration_date':DatePickerInput(),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:99%', }),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:99%', }),
            'date_of_birth':DatePickerInput( attrs={'class': 'form-control','style':'width:88%'}),
            'gender': forms.Select(attrs={'class': 'form-select', 'style': 'width:99%'}),
        }   
        
        
class VitalForm(forms.ModelForm):
    class Meta:
        model = Vital
        fields = "__all__"
        widgets = {
            # 'precio': forms.CharField(widget=forms.NumberInput),

            'patient_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:99%'}),
            ' patient_visit_date': forms.DateField(),
            ' patient_height_in_center_metres': forms.FloatField(),
            'patient_weight_in_kg': forms.FloatField(),
            ' patient_Bmi': forms.FloatField( ),
        }
        

class VisitForm(forms.ModelForm):
    class Meta:
        model=Visit
        fields= "__all__"
        
        Widgets={
            'weight_choice': forms.RadioSelect(choices=DietChoices,)
        }
        