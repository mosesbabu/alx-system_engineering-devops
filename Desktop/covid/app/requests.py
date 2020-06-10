from .model import Country
import urllib.request,json
import requests
from config import Config


# Getting the movie base url
Countries_url = None
Kenyan_url=None
def configure_request(app):
    global Countries_url
    Countries_url = app.config['COUNTRIES_BASE_URL']
    # Kenyan_url=app.config['KENYAN_BASE_URL']

def get_all():
    pass
def get_countries(country_list): 
    url = Countries_url

    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)
   
    data = response.json()
  
    country_results = []
    for country_item in data:
        print(country_item)
        country =country_item.get('country')
        cases =country_item.get('cases') 
        todayCases = country_item.get('todayCases')
        todayDeath =country_item.get('todayDeath') 
        recovered =country_item.get('recovered') 
        active =country_item.get('active') 
        critical =country_item.get('Critical') 
        totalTests =country_item.get('totalTests') 
        country_object = Country(country,cases,todayCases,todayDeath,recovered,active,critical,
        totalTests)
        country_results.append(country_object)
            

    return country_results


def search_country(country_name):
    search_country_url = 'https://coronavirus-19-api.herokuapp.com/countries/{}'.format(country_name)
    with urllib.request.urlopen(search_country_url) as url:
        search_movie_data = url.read()
        search_movie_response = json.loads(search_country_data)

        search_movie_results = None

        if search_country_response['results']:
            search_country_list = search_country_response['results']
            search_country_results = process_results(search_country_list)


    return search_country_results     

