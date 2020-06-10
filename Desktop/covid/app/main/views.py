from flask import render_template,request,redirect,url_for,abort
from . import main
from ..requests import get_countries
from ..model import Country
from flask_login import login_required
from ..corona import Coronavirus

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title='Covid19-updates'
    

    return render_template('index.html', title = title )

@main.route('/allcountries/')
def allcountries():

    '''
    View root page function that returns the index page and its data
    '''
    title='Updates :: allcountries'
    covid_results=get_countries('country')

    return render_template('allstats.html', title = title, countries=covid_results ) 
'''
@main.route('/countries/<country>')
def search_country(country_name):
movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f'search results for {movie_name}'
    return render_template('search.html',movies = searched_movies)
    
    View root page function that returns the index page and its data
    
    
    return render_template('search.html', title = title, results=result )    
'''

@main.route('/subscribe/',methods = ['POST','GET'])
@login_required
def subscribe():
    email = request.form.get('subscriber')
    new_subscriber = Subscriber(email = email)
    new_subscriber.save_subscriber()
    corona=Coronavirus()
    mail_message("Coronavirus stats in your country today!'","email/welcome_subscriber",new_subscriber.email,new_subscriber=new_subscriber,corona=corona)
    flash('Sucessfuly subscribed')
    return redirect(url_for('main.index'))    