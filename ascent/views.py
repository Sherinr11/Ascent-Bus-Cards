
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from ascent.models import *
import requests
from file import file
import json





def index(request):
    if request.session.get('user'):
         return render(request=request, template_name = 'ascent/index.html',context = {})
    else:
        return redirect('userlogin')
    

def signup(request):

    return render(request, 'ascent/signup.html')

def recharge(request):
    if request.session.get('user'):
        return render(request, 'ascent/recharge.html')
    else:
        return redirect('userlogin')
    
def payment(request):
    if  request.method=='POST':
        amt=request.POST['amount']
        context={'amount':amt}
        
    return render(request,'ascent/payment.html',context=context)


def profile(request):
    if request.session.get('user'):
        userprofile = request.session.get('user')
        print(userprofile)
        
        try:
            logged_in_user = userprofile
            user_details = NewUser.objects.get(name=logged_in_user)
            c = user_details.cardno
            p = user_details.phone
            
            
            # Make API request to retrieve balance
            data = {'cardid': c}
            headers = {
        'Authorization': f'Bearer {file.secret_key}',  # Use Bearer token authentication
        # Other headers as needed
    }
            response = requests.post('https://ascent.pythonanywhere.com/bal', data=data,headers=headers)
            
            if response.status_code == 200:
                balance = response.json().get('balance')
            else:
                balance = 'N/A' 

            context = {
                'name': logged_in_user,
                'phone': p,
                'cardid': c,
                'balance': balance
            }
            print(context)
            return render(request, 'ascent/profile.html', context=context)
            
        except NewUser.DoesNotExist:
            return render(request, 'ascent/profile.html', {'error_message': 'User does not exist'})
        except Exception as e:
            return render(request, 'ascent/profile.html', {'error_message': f'Error: {e}'})

     
    else:
        return redirect('userlogin')
    



def transaction(request):
    if request.session.get('user'):
        try:
            userprofile = request.session.get('user')
            card = NewUser.objects.get(name=userprofile).cardno
            
            headers = {
        'Authorization': f'Bearer {file.secret_key}',  # Use Bearer token authentication
        # Other headers as needed
    }
            response = requests.post('https://ascent.pythonanywhere.com/travels', data={'cardid':card},headers=headers)
            if response.status_code == 200:
                travels_df = response.json()
                if 'travels' in travels_df:
        
                    print(travels_df['travels'])
                    return render(request, 'ascent/transaction.html', {'travels': travels_df['travels']})
                else:
                    print("No travel history found")
            else:
                print("Request failed with status code:", response.status_code)
        
        except NewUser.DoesNotExist:
            return render(request, 'ascent/transaction.html', {'error_message': 'User does not exist'})
        except Exception as e:
            return render(request, 'ascent/transaction.html', {'error_message': f'Error: {e}'})        
    else:
        return redirect('userlogin')
    

def userlogout(request):
    del  request.session['user']
    return render(request, 'ascent/login.html')

def userlogin(request):
    if request.method=='POST':
        user=request.POST['username']
        passkey=request.POST['password']
        try:
            user_obj = NewUser.objects.get(name=user)
            if check_password(passkey, user_obj.password):
                request.session['user'] = user
                return redirect(index) 
            else:
                print('Wrong password')
        except NewUser.DoesNotExist:
            print('User does not exist')
        except Exception as e:
            print(f'Error: {e}')
    
    return render(request, 'ascent/login.html')
        
    
    
def usersign(request):
     if request.method=='POST':
        user=request.POST['name']
        passkey1=request.POST['password']
        passkey = make_password(passkey1)
        phone=request.POST['phone']
        cardno=request.POST['cardid']
        try:
 
            new_user = NewUser(name=user, password=passkey, phone=phone, cardno=cardno)
            new_user.save()

        except Exception as e:
            print(f"Error creating NewUser: {e}")



        return redirect('userlogin')