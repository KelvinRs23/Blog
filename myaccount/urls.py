from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('categories/', views.category, name='categories'),
    path('horror/', views.horror, name="horror"),
    path('comedy/', views.comedy, name="comedy"),
    path('romance/', views.romance, name="romance"),
    path('upload/', views.upload, name="upload"),
    path('button/', views.button, name="button"),
    path('about/', views.about, name="about"), 
    path('contact/', views.contact, name="contact"),
    path('film/add/', views.create_film, name='create_film'),
    path('film/list/', views.film_list, name='film_list'),
    path('category/add/', views.create_category, name='create_category'),
    path('category/list/', views.category_list, name='category_list'),
]