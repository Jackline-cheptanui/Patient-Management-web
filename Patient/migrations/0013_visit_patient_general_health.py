# Generated by Django 4.0.6 on 2022-07-29 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0012_remove_visit_general_health_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='patient_general_health',
            field=models.CharField(choices=[('good', 'Good'), ('poor', 'Poor')], max_length=17, null=True),
        ),
    ]