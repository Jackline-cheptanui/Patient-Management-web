# Generated by Django 4.0.6 on 2022-07-29 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0015_alter_patient_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vital',
            name='patient_Bmi',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vital',
            name='patient_height_in_center_metres',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vital',
            name='patient_weight_in_kg',
            field=models.IntegerField(),
        ),
    ]
