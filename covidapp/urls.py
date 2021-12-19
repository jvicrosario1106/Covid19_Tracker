from django.urls import path
from . import views

urlpatterns = [

    path("covid-19/", views.covid19, name="covid19")

]