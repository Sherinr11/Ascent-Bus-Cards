from django.urls import path
from ascent import views

urlpatterns = [
 
     path(route= 'index/', view= views.index, name='index'),
    path('signup/', views.signup, name='signup'),
     path('recherge/', views.recharge, name='recharge'),  
    path('profile/', views.profile, name='profile'),
    path('transaction/', views.transaction, name='transaction'),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('usersign/',views.usersign,name='usersign'),
    path('payment/',views.payment,name='payment')
   
]