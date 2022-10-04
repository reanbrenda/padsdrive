
from cgitb import html
from django.urls import path,re_path
from .import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    re_path(r'^.*\.*', views.pages, name='pages'),
    path('', views.createPadDriveGroup, name='group'),
    path('', views.Paddrivegroup_list, name=''),
    
    
]
