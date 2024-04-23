from django.urls import path
from . import views

urlpatterns = [
    path('bus_operator_dashboard', views.bus_operator_dashboard, name='bus_operator_dashboard'),
    path('logout', views.logout, name='logout'),
    path('bussignup',views.bussignup,name='bussignup'),
    path('buslogin',views.buslogin,name='buslogin')
    
]