from django.shortcuts import render
import requests


def home(request):
    geodata = requests.get("http://ip-api.com/json/").json()
    return render(request, 'core/home.html', {
        'ip': geodata['query'],
        'country': geodata['country'],
        'latitude': geodata['lat'],
        'longitude': geodata['lon'],
        'api_key': 'AIzaSyDGb_yVhVBRTn2wNI2lcQ2M1FAbTXcrfik'
    })


def github(request):
    search_result = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url = 'https://api.github.com/users/%s' % username
        response = requests.get(url)
        search_was_successful = (response.status_code == 200)  # 200 = SUCCESS
        search_result = response.json()
        search_result['success'] = search_was_successful
        search_result['rate'] = {
            'limit': response.headers['X-RateLimit-Limit'],
            'remaining': response.headers['X-RateLimit-Remaining'],
        }
    return render(request, 'core/github.html', {'search_result': search_result})
