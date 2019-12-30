from django.urls import path 
from . import views

urlpatterns = [
	path("",views.project_index.html, name = "project_index"),
	path("<int:pk/", views.project_detail.html, name = "project_detail")
	]