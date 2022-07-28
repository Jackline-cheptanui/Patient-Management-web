from rest_framework import serializers
from Patient.models import Patient
from Patient.models import Visit
from Patient.models import Vital


from Patient.models import Vital,Visit

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields=('patient_number','last_name','first_name')

class VitalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vital
        fields=(' patient_name','patient_visit_date')

class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model=Visit
        fields=('comments',' general_health')
