from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.hashers import check_password,make_password

from busop.models import *
# Create your views here.
def bus_operator_dashboard(request):
    if request.session.get('user'):
        return render(request, 'busop/busop.html')
    else:
        return redirect('buslogin')
    
def logout(request):
    #logout(request)
    # Redirect to the desired page after logout, for example, the index page
    del  request.session['user']
    return render(request,'busop/buslogin.html')
def buslogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
                bus_user = Busop.objects.get(username=username)
                
                if check_password(password, bus_user.password):
                    request.session['user']=username
                    return redirect('bus_operator_dashboard')
        except Busop.DoesNotExist:
            
        
            return render(request, 'busop/buslogin.html', {'error_message': 'Invalid username or password'})
              
    else:    
        return render(request,'busop/buslogin.html')
def bussignup(request):
        if request.method=='POST':
            user=request.POST['name']
            passkey1=request.POST['password']
            passkey = make_password(passkey1)
            phone=request.POST['phone']
            try:
    
                new_user = Busop(username=user, password=passkey, phone=phone)
                new_user.save()
            

            except Exception as e:
                print(f"Error creating NewUser: {e}")
            return  redirect('buslogin')


        return render(request,'busop/bussignup.html')