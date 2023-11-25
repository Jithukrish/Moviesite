from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    # path('login_ren', views.login_ren, name='login_ren'),
    path('logout', views.logout, name='logout'),



    
    
    path('contactus', views.contactus, name='contactus'),
    path('crime', views.crime, name='crime'),
    path('comedy', views.comedy, name='comedy'),
    path('documentary', views.documentary, name='documentary'),
    path('drama', views.drama, name='drama'),

    path('fantasy', views.fantasy, name='fantasy'),
    path('kids', views.kids, name='kids'),
    path('movie_min', views.movie_min, name='movie_min'),
    path('movies', views.movies, name='movies'),
    path('dummy', views.dummy, name='dummy'),
    path('horror', views.horror, name='horror'),
    path('faq', views.faq, name='faq'),


    path('tv', views.tv, name='tv'),
    path('news', views.news, name='news'),
    path('popular', views.popular, name='popular'),
    path('premium', views.premium, name='premium'),
    path('quiz', views.quiz, name='quiz'),
    path('romance', views.romance, name='romance'),
    path('action', views.action, name='action'),
    path('war', views.war, name='war'),
    path('suspense', views.suspense, name='suspense'),
    path('signup', views.signup, name='signup'),
    path('anime', views.anime, name='anime'),
    path('comedy', views.comedy, name='comedy'),
    path('web_series', views.web_series, name='web_series'),
    path('logout', views.logout, name='logout'),
    






]
