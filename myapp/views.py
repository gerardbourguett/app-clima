from django.shortcuts import render
import requests

# Create your views here.


def obtener_clima(ciudad, dias):
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
    querystring = {"q": ciudad, "days": dias}
    headers = {
        "X-RapidAPI-Key": "7b81b72228mshcf22ecf1a65c3e3p11720djsn8e421da9f90a",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com",
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        clima = response.json()
        return clima
    except requests.exceptions.RequestException as e:
        print("Error al obtener el clima:", e)
        return None


def index(request):
    ciudad = request.GET.get("ciudad")
    clima = obtener_clima(ciudad, dias="5")
    return render(request, "index.html", {"clima": clima})
