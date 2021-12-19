from django.shortcuts import render
import json
import urllib.request
from django.http import HttpResponse
# Create your views here.

def covid19(request):

    fetch_url = urllib.request.urlopen("https://api.covid19api.com/summary").read()
    to_json = json.loads(fetch_url)

    countries = to_json["Countries"]

    #EACH COUNTRIES
    country = []
    NewConfirmed = []
    TotalConfirmed = []
    NewDeaths = []
    TotalDeaths = []
    NewRecovered = []
    TotalRecovered = []

    for c in countries:
        country.append(c["Country"])
        NewConfirmed.append(c["NewConfirmed"])
        TotalConfirmed.append(c["TotalConfirmed"])
        NewDeaths.append(c["NewDeaths"])
        TotalDeaths.append(c["TotalDeaths"])
        NewRecovered.append(c["NewRecovered"])
        TotalRecovered.append(c["TotalRecovered"])

    
    summary = zip(country,NewConfirmed,TotalConfirmed,NewDeaths,TotalDeaths,NewRecovered,TotalRecovered)
    print(summary)

    content = {
        "NewConfirmed":str(to_json["Global"]["NewConfirmed"]),
        "TotalConfirmed":str(to_json["Global"]["TotalConfirmed"]),
        "NewDeaths":str(to_json["Global"]["NewDeaths"]),
        "TotalDeaths":str(to_json["Global"]["TotalDeaths"]),
        "NewRecovered":str(to_json["Global"]["NewRecovered"]),
        "TotalRecovered":str(to_json["Global"]["TotalRecovered"]),
        "summary":summary
        
    }




    return render(request, "covidapp/home.html",content)