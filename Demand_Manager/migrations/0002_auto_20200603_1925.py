# Generated by Django 3.0.4 on 2020-06-03 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Demand_Manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demand_master',
            name='Client_Interview_Date',
        ),
        migrations.RemoveField(
            model_name='demand_master',
            name='Client_Screening_Date',
        ),
        migrations.RemoveField(
            model_name='demand_master',
            name='GAVS_Screening_Date',
        ),
        migrations.RemoveField(
            model_name='demand_master',
            name='Onboard_Initated_Date',
        ),
        migrations.RemoveField(
            model_name='demand_master',
            name='Selected_Date',
        ),
    ]
