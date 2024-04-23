from django.shortcuts import render,redirect
from adminpage.urls import *
from adminpage.models import *
from django.contrib.auth.hashers import check_password
from django.contrib import messages
import requests
import json
from file import file


def adminloginPageView(request):
    return render(request,'adminpage/adlogin.html',context={})
def logout_view(request):
    del request.session['user']
    return redirect('login')
def admin_login(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            try:
                admin_user = Admin.objects.get(username=username)
                if check_password(password, admin_user.password):
                    request.session['user']=username
                    return redirect('admin_dashboard')
            except Admin.DoesNotExist:
        
                return render(request, 'adminpage/adlogin.html', {'error_message': 'Invalid username or password'})
            return redirect('admin_dashboard')
    else:
        return render(request, 'adminpage/adlogin.html')
def admindashboard(request):
    if request.session.get('user'):
         return render(request,'adminpage/adduser.html')
    else:
        return redirect('login')
   
def add_user(request):
    if request.method == 'POST':
        try:
        
            cardid = request.POST.get('card-id')
            name = request.POST.get('name')
            amount = request.POST.get('amount')
            email = request.POST.get('mail')
            phone = request.POST.get('phone')
            data = {
                'cardid': cardid,
                'name': name,
                'amount': amount,
                'email': email,
                'phone': phone
            }
            print(data)
            headers = {
    'Authorization': f'Bearer {file.secret_key}',  # Use Bearer token authentication
    # Other headers as needed
}
            response = requests.post('https://ascent.pythonanywhere.com/add', data=data,headers=headers)
            print(response.content)
            print(response.status_code)
            if response.status_code == 200:
                messages.success(request, 'User added successfully.')
            else:
                messages.error(request, 'Failed to add user. Please try again.')
            return redirect('add_user')
        except Exception as e:
            print(f'Error: {e}')
    
    return render(request, 'adminpage/adduser.html')

def user_travel_history(request):
    if request.session.get('user'):
        headers = {
    'Authorization': f'Bearer {file.secret_key}',  # Use Bearer token authentication
    # Other headers as needed
}
        response=requests.get('https://ascent.pythonanywhere.com/allusertravel',headers=headers)
        json_data=response.content
        print(response.status_code)
        travels_data = json.loads(json_data.decode('utf-8'))

        return render(request, 'adminpage/adtrans.html', {'travels_data': travels_data})
            
    else:
        return redirect('login')
    
    