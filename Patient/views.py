
from .models import Patient, Visit, Vital
from django.shortcuts import render
from.forms import VisitForm
from.forms import PatientRegistrationForms
from.forms import VitalForm
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django.views import generic
from .models import Patient

def register_patient(request):
    if request.method== "POST":
        form=PatientRegistrationForms(request.POST,request.FILES,)
        if form.is_valid():
         form.save()
        else:
            print(form.errors)
    else:
        form=PatientRegistrationForms()
    return render(request,"register_patient.html",{"form":form})

def patient_list(request):
    patients=Patient.objects.all()
    return render(request,"patient_list.html",{"patients":patients})  



def vital_register(request):
    if request.method== "POST":
        form=VitalForm(request.POST,request.FILES,)
        if form.is_valid():
         form.save()
        else:
            print(form.errors)
    else:
        form=VitalForm()
    return render(request,"vital_register.html",{"form":form})

def vital_list(request):
    vitals=Vital.objects.all()
    return render(request,"vital_list.html",{"vitals":vitals})  
    

def visit_list(request):
   visits=Visit.objects.all()
   return render(request,"visit_list.html",{"visits":visits})  



        
def visit_register(request):
    if request.method== "POST":
        form=VisitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=VisitForm()
    return render(request,"visit_register.html", {"form":form})