from django.urls import path
from adminpage import views
urlpatterns = [
    path(route= 'login', view= views.adminloginPageView, name='login'),
    path(route='adminlogin',view=views.admin_login,name='adminlogin'),
    path(route='admin_dashboard',view=views.admindashboard,name='admin_dashboard'),
    path(route='add_user/',view= views.add_user, name='add_user'),
    path('user-travel-history/', views.user_travel_history, name='user_travel_history'),
    path('adlogout/', views.logout_view, name='adlogout'),  
   ]