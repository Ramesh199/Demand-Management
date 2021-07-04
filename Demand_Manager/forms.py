from django.forms import ModelForm
from .models import Demand_Master
from django import forms


class DateInput(forms.DateInput):
	input_type= 'date'

class CalendarUtilForm(forms.Form):
	Expected_Start_Date = forms.DateField(widget=DateInput)
	Client_Interview_Date = forms.DateField(widget=DateInput)

class UpdateForm(ModelForm):
	Demand_Id = forms.CharField(label='Demand Id',
				widget=forms.TextInput(attrs={"readonly":"readonly"}))
	Demand_Status = forms.CharField(label='Demand Status',
				widget=forms.TextInput(attrs={"readonly":"readonly"}))


	class Meta:
		model= Demand_Master
		
		fields = [
				'Demand_Id', 
				'Project',
				'Candidate',
				
				'Location',
				'Portfolio', 
				'Demand_Status',
				'Role',
				'Client_Interview_Date',
				'Onshore_Replacement_Flag',
				'Portfolio_Lead',
				'Detailed_Status',
				'Skillset',
				'Client_Feedback',
				'Expected_Start_Date',
				'Hiring_Manager',
				'Notes'
				]
			
		widgets = {'Expected_Start_Date':DateInput(),'Client_Interview_Date':DateInput() }

			
		

