from django.urls import path
from . import views

app_name = 'superheroes'
urlpatterns = [
    path('', views.index, name='index')

]