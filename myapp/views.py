from django.shortcuts import render
import requests

# Create your views here.


def clima(ciudad):
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    querystring = {"q": ciudad}
    headers = {
        "X-RapidAPI-Key": "7b81b72228mshcf22ecf1a65c3e3p11720djsn8e421da9f90a",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com",
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()


def index(request):
    ciudad = request.GET.get("ciudad")
    datos_clima = clima(ciudad)
    return render(request, "index.html", {"clima": datos_clima})
