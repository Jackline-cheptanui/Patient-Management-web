# Generated by Django 4.0.6 on 2022-07-29 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0009_rename_general_heaith_visit_general_health'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visit',
            name='general_health',
        ),
    ]
