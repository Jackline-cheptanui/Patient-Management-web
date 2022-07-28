# Generated by Django 4.0.6 on 2022-07-28 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0005_visit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visit',
            name='weigth_choice',
        ),
        migrations.AddField(
            model_name='visit',
            name='weight_choice',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=17),
        ),
    ]
