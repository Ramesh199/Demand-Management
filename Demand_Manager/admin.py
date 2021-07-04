from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.

@admin.register(Demand_Master)
class ViewAdmin(ImportExportModelAdmin):
	include = ('id', )

class Demand_MasterAdmin(admin.ModelAdmin):
	list_display = ['Fiscal_Year', 
				'Demand_Status', 
				'Demand_Id', 
				'Portfolio', 
				'Portfolio_Lead',
				'Hiring_Manager',
				'Project',
				'Role',
				'Skillset',
				'Location',
				'Onshore_Replacement_Flag',
				'Expected_Start_Date',
				'Detailed_Status',
				'Notes',
				'Candidate',
				'Client_Feedback'
				]
