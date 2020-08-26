from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('trends', views.trends,name='trends'),
    path('data', views.classify,name='data')

]
