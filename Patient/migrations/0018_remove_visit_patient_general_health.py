# Generated by Django 4.0.6 on 2022-07-29 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0017_alter_vital_patient_bmi_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visit',
            name='patient_general_health',
        ),
    ]