# Generated by Django 3.0.4 on 2020-06-03 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Demand_Manager', '0003_auto_20200603_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demand_master',
            name='Candidate',
            field=models.CharField(blank='true', max_length=100),
        ),
        migrations.AlterField(
            model_name='demand_master',
            name='Client_Feedback',
            field=models.CharField(blank='true', max_length=200),
        ),
        migrations.AlterField(
            model_name='demand_master',
            name='Demand_Id',
            field=models.CharField(blank='true', max_length=25),
        ),
        migrations.AlterField(
            model_name='demand_master',
            name='Demand_Status',
            field=models.CharField(blank='true', choices=[('Open', 'Open'), ('In - Progress', 'In - Progress'), ('On - Hold', 'On - Hold'), ('Cancelled', 'Cancelled'), ('Closed', 'Closed')], max_length=25),
        ),
        migrations.AlterField(
            model_name='demand_master',
            name='Detailed_Status',
            field=models.CharField(blank='true', choices=[('1 - GAVS Sourcing/Screening', '1 - GAVS Sourcing/Screening'), ('2 - Premier Reviewing Profiles', '2 - Premier Reviewing Profiles'), ('3 - Premier Interviewing', '3 - Premier Interviewing'), ('4 - Candidate Selected', '4 - Candidate Selected'), ('5 - Onboarding in Progress', '5 - Onboarding in Progress'), ('7 - Candidate Started', '7 - Candidate Started'), ('8 - On Hold', '8 - On Hold'), ('9 - Cancelled', '9 - Cancelled')], max_length=50),
        ),
        migrations.AlterField(
            model_name='demand_master',
            name='Fiscal_Year',
            field=models.CharField(blank='true', max_length=4),
        ),
        migrations.AlterField(
            model_name='demand_master',
            name='Hiring_Manager',
            field=models.CharField(blank='true', max_length=50),
        ),
        migrations.AlterField(
            model_name='demand_master',
            name='Location',
            field=models.CharField(blank='true', choices=[('Off', 'Off'), ('On', 'On'), ('On-Off', 'On-Off')], max_length=10),
        ),
        migrations.AlterField(
            model_name='demand_master',
            name='Notes',
            field=models.TextField(blank='true'),
        ),
        migrations.AlterField(
            model_name='demand_master',
            name='Portfolio',
            field=models.CharField(blank='true', choices=[('Clinical Decision Support', 'Clinical Decision Support'), ('Clinical Survelliance', 'Clinical Survelliance'), ('Contigo Health', 'Contigo Health'), ('Corp IT', 'Corp IT'), ('Cost Management', 'Cost Management'), ('Development Operations', 'Development Operations'), ('GPO', 'GPO'), ('Infrastructure', 'Infrastructure'), ('Innovatix', 'Innovatix'), ('IPA', 'IPA'), ('Population Health', 'Population Health'), ('PAS', 'PAS'), ('Quality & Population Health', 'Quality & Population Health')], max_length=100),
        ),
        migrations.AlterField(
            model_name='demand_master',
            name='Portfolio_Lead',
            field=models.CharField(blank='true', choices=[('Alex Tatiyants', 'Alex Tatiyants'), ('Chris Ickert', 'Chris Ickert'), ('Denise Juliano', 'Denise Juliano'), ('Greg Montano', 'Greg Montano'), ('Pawan Singh', 'Pawan Singh'), ('Saima Khan', 'Saima Khan'), ('Saji Rajasekharan', 'Saji Rajasekharan'), ('Todd Wilkes', 'Todd Wilkes')], max_length=50),
        ),
        migrations.AlterField(
            model_name='demand_master',
            name='Project',
            field=models.CharField(blank='true', max_length=100),
        ),
        migrations.AlterField(
            model_name='demand_master',
            name='Role',
            field=models.CharField(blank='true', max_length=100),
        ),
        migrations.AlterField(
            model_name='demand_master',
            name='Skillset',
            field=models.CharField(blank='true', max_length=100),
        ),
    ]