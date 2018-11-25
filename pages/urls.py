from django.urls import path

# I think this . means current folder
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about')
]