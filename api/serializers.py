from rest_framework import serializers
from patient.models import Patient
from vital.models import Vital
from visit.models import Visit


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields=('patient_number','last_name','first_name')

class VitalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Visit
        fields=(' patient_name','patient_visit_date')


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model=Visit
        fields=('comments',' general_health')

