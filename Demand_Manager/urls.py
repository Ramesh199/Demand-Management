from django.urls import path
from . import views

app_name = 'Demand_Manager'

urlpatterns = [
    path('', views.home, name="home"),
    path("active_demands/", views.activeDemands, name="active_demands"),
    path("all_demands/", views.allDemands, name="all_demands"),
    path("inprogress_noupdates/", views.inprogressNoupdates, name="inprogress_noupdates"),   
    path("inprogress_noupdates/<str:pk>/update_detail10/", views.updateDetail10, name="update_detail10"),
    path("active_demands/<str:pk>/update_detail/", views.updateDetail, name="update_detail"),
    path("active_ageing/", views.activeAeging, name="active_ageing"),
    path("onboard_inprogress/", views.onboardInprogress, name="onboard_inprogress"),
    
    path("about/", views.aboutD, name="about"),

]