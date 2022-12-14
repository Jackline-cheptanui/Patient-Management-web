# Generated by Django 4.0.6 on 2022-07-29 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0020_alter_visit_patient_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='id',
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_number',
            field=models.BigAutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='visit',
            name='patient_general_health',
            field=models.CharField(choices=[('Good', 'Good'), ('Poor', 'Poor')], max_length=17, null=True),
        ),
    ]
