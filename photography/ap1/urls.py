from django.urls import path
from . import views





urlpatterns = [
    path('', views.home,name='home_page'),
    path('first/', views.first,name='login_page'),
    
]