import datetime
from django.shortcuts import render
from django.contrib import messages
import requests

def home(request):
    details ={'Flag':True}
    if request.method == 'POST':
        city = request.POST.get('value')
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=241bc9a407a7565c4e826f1fbf47c197&units=metric".format(city)
        res = requests.get(url)
        data = res.json()
        if data["cod"] != "404":

            temp = data['main']['temp']
            ftemp = (temp * 9/5) + 32.
            ftemp = float("{:.2f}".format(ftemp))
            temp_min = data['main']['temp_min']
            temp_max = data['main']['temp_max']

            feels_like = data['main']['feels_like']
            pressure = data['main']['pressure']
            weather = data['weather'][0]['main']
            description = data['weather'][0]['description']

            humidity = data['main']['humidity']
            country = data['sys']['country']
            speed = data['wind']['speed']
            icon = data['weather'][0]['icon']

            iicon = ('http://openweathermap.org/img/w/{}.png').format(icon)

            clouds = data['clouds']['all']
            sunrise = data['sys']['sunrise']
            sunset = data['sys']['sunset']
            sunrise = datetime.datetime.fromtimestamp(sunrise)
            sunset = datetime.datetime.fromtimestamp(sunset)
            hometime = sunrise.strftime('%d %b | %Y')

            details = {'phometime': hometime, 'psunrise': sunrise, 'psunset': sunset, 'pcountry': country, 'picon': iicon,
                       'pcity': city.capitalize(), 'ptemp': temp, 'ftemp':ftemp,'ptemp_min': temp_min, 'ptemp_max': temp_max,
                       'pfeels_like': feels_like,'ppressure': pressure, 'pspeed': speed, 'pweather': weather,
                       'pdescription': description,'phumidity': humidity, 'pclouds': clouds,'hometime':hometime,'Flag':False}

        else:
            messages.error(request, ' SORRY! NO CITY FOUND !!!')

    print(details['Flag'])
    return render(request, 'pingoweather/home.html', details)





