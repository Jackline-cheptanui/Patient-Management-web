# Generated by Django 4.0.6 on 2022-07-28 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0006_remove_visit_weigth_choice_visit_weight_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visit',
            name='comment',
        ),
        migrations.AddField(
            model_name='visit',
            name='comments',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
