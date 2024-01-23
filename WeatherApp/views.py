from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
import urllib.request


def city_data(city):
    city = city.lower()
    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=0ac45593d4c7e3c1638e35f610b3fcf9'
    try :
        data = urllib.request.urlopen(url).read()
        list_of_data = json.loads(data)
        return {
            "city": str.capitalize(city),
            "country": str(list_of_data['sys']['country']),
            "sunrise": str(list_of_data['sys']['sunrise']),
            "sunset": str(list_of_data['sys']['sunset']),
            "timezone": str(list_of_data['timezone']),
            "name": str(list_of_data['name']),
            "clouds": str(list_of_data['clouds']['all']),
            "wind_speed": str(list_of_data['wind']['speed']),
            "coordinates": str(list_of_data['coord']['lon']) + ',' + str(list_of_data['coord']['lat']),
            "temperature": str(list_of_data['main']['temp']) + '°C',
            "temperature_min": str(list_of_data['main']['temp_min']) + '°C',
            "temperature_max": str(list_of_data['main']['temp_max']) + '°C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            # "sea_level": str(list_of_data['main']['sea_level']),
            "base": str(list_of_data['base']),
            "forecast": str(list_of_data['weather'][0]['main']),
            "description": str(list_of_data['weather'][0]['description']),
            "icon": str(list_of_data['weather'][0]['icon'])
        }

    except Exception as e:
        print(f"Error fetching data: {e}")
        return None


def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        data = city_data(city)
        if data:
            return render(request, 'index.html', data)
        else:
            error_message = "Incorrect city name or unable to fetch data."
            return render(request, 'index.html', {'error_message': error_message})
    else:
        data = {}
        return render(request, 'index.html', data)



def full_details(request):
    city_name = request.GET.get('cityName', '')
    data = city_data(city_name)
    return render(request, 'details.html', data)
