from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Demand_Master
from django.db.models import Count, Sum
from datetime import date, timedelta, datetime
from django.contrib import messages
from .forms import UpdateForm
import numpy as np
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models.functions import Lower

def home(request):
	
	now = datetime.now().date()
	earlier = now - timedelta(days=7)
	now = now.strftime('%Y-%m-%d')
	earlier = earlier.strftime('%Y-%m-%d')
	date_format = "%Y-%m-%d"
	sysdate = datetime.strptime(str(datetime.now().date()), date_format)

	context = {
	"By_Status_Location_dict":Demand_Master.objects.
	exclude(Demand_Status = "Closed").
	exclude(Demand_Status = "Cancel").
	exclude(Demand_Status = "Hold").
	values('Demand_Status', 'Location').
	annotate(total=Count('id')).
	order_by('Demand_Status', 'Location'),

	"By_Detailed_Status_dict":Demand_Master.objects.
	values('Detailed_Status').
	order_by('Detailed_Status').
	annotate(total=Count('id')),

	"By_Gtotal_dict":Demand_Master.objects.
	annotate(total = Count('Detailed_Status')).
	aggregate(gtotal = Sum('total')),
	
	"Demand_Wk_Interviewed_dict": Demand_Master.objects.
	filter(Log_Date__gte = earlier, Detailed_Status = '3 - Premier Interviewing'),
	
	"Demand_Wk_Selected_dict": Demand_Master.objects.
	filter(Log_Date__gte = earlier, Detailed_Status = '4 - Candidate Selected'),
	
	"Demand_Wk_Started_dict": Demand_Master.objects.
	filter(Actual_Start_Date__gte = earlier, Detailed_Status = '7 - Candidate Started')
	}

	return render(request, 'Demand_Manager/dashboard.html', context)

def allDemands(request):
	
	order_by = request.GET.get('order_by')
	direction = request.GET.get('direction')
	ordering = Lower(order_by)

	if direction == 'desc':
		ordering = '-{}'.format(ordering)

	All_Demands_Dict = Demand_Master.objects.all().order_by(ordering)
	
	paginator = Paginator(All_Demands_Dict, 15)
	page = request.GET.get('page')

	try:
		all_All_Demands_Dict = paginator.page(page)
	except PageNotAnInteger:
		all_All_Demands_Dict = paginator.page(1)
	except EmptyPage:
		all_All_Demands_Dict = paginator.page(paginator.num_pages)

	return render(request,
				  "Demand_Manager/alldemands.html",
				  context = {'all_All_Demands_Dict':all_All_Demands_Dict,
				  'order_by': order_by, 'direction': direction
				  }
				  )

def activeDemands(request):

	return render(request,
				  "Demand_Manager/activedemands.html",
				  context = {"Demand_Active_Dict":Demand_Master.objects.exclude(Demand_Status = "Closed").exclude(Demand_Status = "Cancel").order_by('Demand_Status', 'Demand_Id', 'Location', 'Requested_Date')
				  }
				  )

def updateDetail(request, pk):
	
	detail = Demand_Master.objects.get(id=pk)
	form = UpdateForm(instance=detail)
	if request.method == 'POST':
		form = (UpdateForm(request.POST, instance=detail))
		error = 'no'
		if form.is_valid():
			nform = form.save(commit=False)
			
			if nform.Detailed_Status == '7 - Candidate Started':
				nform.Demand_Status = 'Closed'
			
			if nform.Detailed_Status != '1 - GAVS Sourcing/Screening':
				if nform.Demand_Status == "Open":
					nform.Demand_Status = 'In - Progress'

			if nform.Detailed_Status == '2 - Premier Reviewing Profiles':
					nform.Client_Screening_Date = datetime.now().date()

			if nform.Detailed_Status == '3 - Premier Interviewing':
				print(nform.Detailed_Status +'is'+ nform.Candidate)
				print(nform.Detailed_Status +'is'+ nform.Candidate)
				if nform.Candidate == '':
					messages.info(request, "Candidate name cannot be blank")
					error = 'yes'
				if nform.Client_Interview_Date == None:
					messages.info(request, "Interview Date cannot be blank")
					error = 'yes'
			if nform.Detailed_Status == '8 - On Hold':
				nform.Demand_Status = 'On - Hold'
			
			
			if error != 'yes':
				nform.save()
				messages.success(request, f"Demand details updated successfully")
				return redirect("Demand_Manager:active_demands")
			
	context = {'form':form}
	return render(request, "Demand_Manager/update_Detail.html", context)

def inprogressNoupdates(request):
	number_of_days = 10
	to_date = date.today()
	while number_of_days:
		to_date -= timedelta(1)
		if to_date.weekday() < 5:
			number_of_days -= 1
    
	
	return render(request,
				  "Demand_Manager/inprogressnoupdates.html",
				  context = {"Demand_Noupdates_Dict":Demand_Master.objects.filter(Demand_Status = "In - Progress", Log_Date__lte = to_date).order_by('Portfolio', 'Location', '-Demand_Status')
				  }
				  )

def updateDetail10(request, pk):
	
	detail = Demand_Master.objects.get(id=pk)
	form = UpdateForm(instance=detail)
	if request.method == 'POST':
		form = (UpdateForm(request.POST, instance=detail))
		error = 'no'
		if form.is_valid():
			nform = form.save(commit=False)
			
			if nform.Detailed_Status != '1 - GAVS Sourcing/Screening':
				if nform.Demand_Status == "Open":
					nform.Demand_Status = 'In - Progress'

			if nform.Detailed_Status == '8 - On Hold':
				nform.Demand_Status = 'On - Hold'
			if nform.Demand_Status == "On - Hold":
					nform.Detailed_Status = '8 - On Hold'

			if nform.Detailed_Status == '2 - Premier Reviewing Profiles':
				if nform.Client_Screening_Date == None:
					nform.Client_Screening_Date = datetime.now().date()

			if nform.Detailed_Status == '3 - Premier Interviewing':
				if nform.Candidate == '':
					messages.info(request, "Candidate name cannot be blank")
					error = 'yes'

			if error != 'yes':
				nform.save()
				messages.success(request, f"Demand details updated successfully")
				return redirect("Demand_Manager:inprogress_noupdates")
			
			
	context = {'form':form}
	return render(request, "Demand_Manager/update_Detail10.html", context)

def activeAeging(request):
	
	return render(request,
				  "Demand_Manager/top20ageingdemands.html",
				  context = {"Demand_Ageing_Dict":Demand_Master.objects.
				  filter(Q(Demand_Status = "In - Progress") | Q(Demand_Status = "Open")).
				  order_by('Requested_Date', 'Location', 'Portfolio', 'Demand_Status')[:20]
				  }
				  )

def onboardInprogress(request):
	
	return render(request,
				  "Demand_Manager/onboardinprogress.html",
				  context = {"Onboard_Inprogress_Dict":Demand_Master.objects.
				  filter(Detailed_Status = "5 - Onboarding in Progress").
				  order_by('Requested_Date', 'Location', 'Portfolio', 'Demand_Status')[:20]
				  }
				  )

def aboutD(request):
	
	return render(request,
				  "Demand_Manager/about.html"
				  )

	