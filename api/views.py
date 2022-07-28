from django.shortcuts import render
from django import Serializer
from rest_framework import viewsets
from web_Application.Patient.models import Patient, Visit, Vital
class PatientViewSet(viewsets.ModelViewSet):
    queryset=Patient.objects.all()
    serializer_class=PersonSerializer

class VitalViewSet(viewsets.ModelViewSet):
    queryset=Vital.objects.all()
    serializer_class=VitalSerializer
class VisitViewSet(viewsets.ModelViewSet):
    queryset=Visit.objects.all()
    serializer_class=VisitSerializer

