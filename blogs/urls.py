from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"), 
    path('horror/', views.horror, name="horror"),
    path('comedy/', views.comedy, name="comedy"),
    path('romance/', views.romance, name="romance"),
    path('upload/', views.upload, name="upload"),
    path('button/', views.button, name="button"),
    path('about/', views.about, name="about"), 
    path('contact/', views.contact, name="contact"), 


]