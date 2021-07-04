from django.db import models
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.utils.timezone import now
import numpy as np
import datetime as dt


class Demand_Master(models.Model):
	
	STATUS =(
	    ('Open', 'Open'),
	    ('In - Progress', 'In - Progress'),
	    ('On - Hold', 'On - Hold'),
	    ('Cancelled', 'Cancelled'),
	    ('Closed', 'Closed')
	)


	PORTFOLIO = (
	        ('Clinical Decision Support', 'Clinical Decision Support'),
	        ('Clinical Survelliance', 'Clinical Survelliance'),
	        ('Contigo Health', 'Contigo Health'),
	        ('Corp IT', 'Corp IT'),
	        ('Cost Management', 'Cost Management'),
	        ('Development Operations', 'Development Operations'),
	        ('GPO', 'GPO'),
	        ('Infrastructure', 'Infrastructure'),
	        ('Innovatix', 'Innovatix'),
	        ('IPA', 'IPA'),
	        ('Population Health', 'Population Health'),
	        ('PAS', 'PAS'),
	        ('Quality & Population Health', 'Quality & Population Health'),
	        ('Clinical Performance Improvement', 'Clinical Performance Improvement')
	)


	PLEAD = (
	        ('Alex Tatiyants', 'Alex Tatiyants'),
	        ('Chris Ickert', 'Chris Ickert'),
	        ('Denise Juliano', 'Denise Juliano'),
	        ('Greg Montano', 'Greg Montano'),
	        ('Pawan Singh', 'Pawan Singh'),
	        ('Saima Khan', 'Saima Khan'),
	        ('Saji Rajasekharan', 'Saji Rajasekharan'),
	        ('Todd Wilkes', 'Todd Wilkes'),
	        ('Charlie Sinnett', 'Charlie Sinnett')
	)

	LOCATION = (
        ('Off', 'Off'),
        ('On', 'On'),
        ('On-Off', 'On-Off')
    )

	RFLAG = (
	        ('Yes', 'Yes'),
	        ('No', 'No'),
	        ('N/A', 'N/A')
	)

	DSTATUS = (
        ('1 - GAVS Sourcing/Screening', '1 - GAVS Sourcing/Screening'),
        ('2 - Premier Reviewing Profiles', '2 - Premier Reviewing Profiles'),
        ('3 - Premier Interviewing', '3 - Premier Interviewing'),
        ('4 - Candidate Selected', '4 - Candidate Selected'),
        ('5 - Onboarding in Progress', '5 - Onboarding in Progress'),
        ('7 - Candidate Started', '7 - Candidate Started'),
        ('8 - On Hold', '8 - On Hold'),
        ('9 - Cancelled', '9 - Cancelled')
    )


	Fiscal_Year = models.CharField(max_length=4, blank='true')
	Requested_Date = models.DateField(default=datetime.now)
	#Days_Open = models.IntegerField(default=0)
	Demand_Status = models.CharField(max_length=25, choices = STATUS, blank='true')
	Demand_Id = models.CharField(max_length=25, blank='true')
	Portfolio = models.CharField(max_length=100, choices = PORTFOLIO, blank='true')
	Portfolio_Lead = models.CharField(max_length=50, choices = PLEAD, blank='true')
	Hiring_Manager = models.CharField(max_length=50, blank='true')
	Project = models.CharField(max_length=100, blank='true')
	Role = models.CharField(max_length=100, blank='true')
	Skillset = models.CharField(max_length=100, blank='true')
	Location = models.CharField(max_length=10, choices = LOCATION, blank='true')
	Onshore_Replacement_Flag = models.CharField(max_length=3, choices = RFLAG, default='N/A')
	Planned_Start_Date = models.DateField(default=datetime.now)
	Expected_Start_Date = models.DateField(default=datetime.now)
	Detailed_Status = models.CharField(max_length=50, choices = DSTATUS, blank='true')
	Notes = models.TextField(blank='true')
	Actual_Start_Date = models.DateField(default=datetime.now)
	Candidate = models.CharField(max_length=100, blank='true')
	Client_Feedback = models.CharField(max_length=200, blank='true')
	GAVS_Screening_Date = models.DateField(null='true', blank='true')
	Client_Screening_Date = models.DateField(null='true', blank='true')
	Client_Interview_Date = models.DateField(null='true', blank='true')
	Selected_Date = models.DateField(null='true', blank='true')
	Onboard_Initated_Date =  models.DateField(null='true', blank='true')
	Log_Date = models.DateField(auto_now='true')

	def __str__(self):
		return self.Demand_Id

	def Days_Open(self):
		Days_Open = np.busday_count(self.Requested_Date, datetime.now().date())
		return Days_Open

	def Days_Ageing(self):
		Days_Ageing = np.busday_count(self.Log_Date, datetime.now().date())
		return Days_Ageing

	def gtotal(self):
		sum = self.id 
		gtotal +=1
		return gtotal
		
	  