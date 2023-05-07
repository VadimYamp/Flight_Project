import datetime
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.template import loader
from django.core import serializers
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from App_A.Data_Layer import *
from App_A.Business_Layer import *




def Home(request):
    _user = None
    if 'user' in request.session:
        _userSession = request.session['user']
        _userList = list(serializers.deserialize("json", _userSession))
        _user = _userList[0].object
        
    template = loader.get_template('Home.html')
    context = {
        'Current_user':     _user,
        'Home':            Home_Page(),
    }
    return HttpResponse(template.render(context, request))

def X_Cust_Account(request):
    template = loader.get_template('X_Cust_Account.html')
    context = {  
    }
    return HttpResponse(template.render(context, request))

def Y_Airline_Account(request):
    template = loader.get_template('Y_Airline_Account.html')
    context = {  
    }
    return HttpResponse(template.render(context, request))

def Z_Admin_Account(request):
    template = loader.get_template('Z_Admin_Account.html')
    context = {  
    }
    return HttpResponse(template.render(context, request))



def Test(request):
    template = loader.get_template('Test.html')
    context = {
        'Test_X': c10_Get_Airlines_By_Country("ישראל"),
        'Test_Y': c10_Get_Airlines_By_Country("רוסיה"),
        'Test_Z': c10_Get_Airlines_By_Country("צרפת"),
    }
    return HttpResponse(template.render(context, request))

#GET
@ensure_csrf_cookie
def R_Cust_Registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        #form.fields['Role'] = 3
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm(initial={'Role': '3'})
    return render(request, 'R_Cust_Registration.html', {'form': form})

@ensure_csrf_cookie
def S_Airline_Registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        #form.fields["Role"] = 2
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'S_Airline_Registration.html', {'form': form})

@ensure_csrf_cookie
def T_Admin_Registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        #form.fields["Role"] = 1
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'T_Admin_Registration.html', {'form': form})

@ensure_csrf_cookie
@csrf_protect
def Login(request):
    if request.method == 'POST':
        
        # validate the CSRF token
        if not request.POST.get('csrfmiddlewaretoken'):
            return HttpResponseBadRequest('Missing CSRF token')
        
        # validate user
        username = request.POST.get('username')
        password = request.POST.get('password')
        _customerService = Customer_Facade()
        _user = _customerService.d01_Login(username, password)
        
        if _user:
            _userSerialized = serializers.serialize("json", _user)
            request.session['user'] = _userSerialized
            
            return redirect('home')
        else:
            request.error = ["User not valid."]
            #form.is_valid = False
            return render(request, 'Login.html', {'form': LoginForm()})
    else:
        form = LoginForm()
    return render(request, 'Login.html', {'form': form})

def Logout(request):
    #logout(request)
    del request.session['user']
    
    response = HttpResponseRedirect(reverse('home'))
    response.delete_cookie('csrftoken')
    return response

# GET request
@ensure_csrf_cookie
def n1_Users_Page(request):
    _user = request.session_user
    if _user and (_user.Role.id != 1):
            return redirect('home')
    
    _user_facade = Administrator_Facade()
    if request.method == 'POST':
    
        # validate the CSRF token
        if not request.POST.get('csrfmiddlewaretoken'):
            return HttpResponseBadRequest('Missing CSRF token')
    
        # Check if the delete button was clicked
        if request.POST.get('delete_id'):
            # Get the object to delete
            _id = request.POST.get('delete_id')
            _role_id = request.POST.get('delete_role_id')
            _user_facade.k04_Remove_User(_id, _role_id)
            
            # Redirect to the same page to avoid resubmission
            return redirect('Users_Page')
          
    template = loader.get_template('n1_Users.html')
    context = {
        'Current_user':     _user,
        'Users':            b01_Get_All_Users(),
    }
    return HttpResponse(template.render(context, request))

@ensure_csrf_cookie
def n2_Customers_Page(request):
    _user = request.session_user
    if _user and _user.Role.id != 1:
        return redirect('home')
    
    _user_facade = Administrator_Facade()
    if request.method == 'POST':
        
        # validate the CSRF token
        if not request.POST.get('csrfmiddlewaretoken'):
            return HttpResponseBadRequest('Missing CSRF token')
        
        # Check if the delete button was clicked
        if request.POST.get('delete_id'):
            # Get the object to delete
            _id = request.POST.get('delete_id')
            _user_facade.k05_Remove_Customer(_id)           
            # Redirect to the same page to avoid resubmission
            return redirect('n2_Customers_Page')  
    template = loader.get_template('n2_Customers.html')
    context = {
        'Current_user':             _user,
        'Customers':             b02_Get_All_Customers(),
    }
    return HttpResponse(template.render(context, request))

@ensure_csrf_cookie
def n3_Airlines_Page(request):
    _user = None
    if 'user' in request.session:
        _userSession = request.session['user']
        _userList = list(serializers.deserialize("json", _userSession))
        _user = _userList[0].object
        
        if _user.Role.id != 1:
            return redirect('home')
    
    _user_facade = Administrator_Facade()
    if request.method == 'POST':
        
        # validate the CSRF token
        if not request.POST.get('csrfmiddlewaretoken'):
            return HttpResponseBadRequest('Missing CSRF token')
        
        # האם כפתור המחיקה נלחץ
        if request.POST.get('delete_id'):
            # הבאת השורה למחיקה
            _id = request.POST.get('delete_id')
            _user_facade.k06_Remove_Airline(_id)           
            # חזרה לטבלה לאחר הפעולה
            return redirect('n3_Airlines_Page')  
    template = loader.get_template('n3_Airline_Companies.html')
    context = {
        'Current_user':      _user,
        'Airline_Companies': b03_Get_All_Airline_Companies(),
    }
    return HttpResponse(template.render(context, request))

def n4_Administrators_Page(request):
    _user = None
    if 'user' in request.session:
        _userSession = request.session['user']
        _userList = list(serializers.deserialize("json", _userSession))
        _user = _userList[0].object
        
        if _user.Role.id != 1:
            return redirect('home')
    
    _user_facade = Administrator_Facade()
    if request.method == 'POST':
        
        # validate the CSRF token
        if not request.POST.get('csrfmiddlewaretoken'):
            return HttpResponseBadRequest('Missing CSRF token')
        
        # האם כפתור המחיקה נלחץ
        if request.POST.get('delete_id'):
            # הבאת השורה למחיקה
            _id = request.POST.get('delete_id')
            _user_facade.k07_Remove_Administrator(_id)           
            # חזרה לטבלה לאחר הפעולה
            return redirect('n4')  
    template = loader.get_template('n4_Administrators.html')
    context = {
        'Current_user':     _user,
        'Administrators':             b04_Get_All_Administrators(),
    }
    return HttpResponse(template.render(context, request))

def n5_User_Roles_Page(request):
    _user = None
    if 'user' in request.session:
        _userSession = request.session['user']
        _userList = list(serializers.deserialize("json", _userSession))
        _user = _userList[0].object
        
        if _user.Role.id != 1:
            return redirect('home')
    
    _user_facade = Administrator_Facade()
    if request.method == 'POST':
        
        # validate the CSRF token
        if not request.POST.get('csrfmiddlewaretoken'):
            return HttpResponseBadRequest('Missing CSRF token')
         
    template = loader.get_template('n5_User_Roles.html')
    context = {
        'Current_user':     _user,
        'User_Roles':             b05_Get_All_User_Roles(),
    }
    return HttpResponse(template.render(context, request))

def n6_Countries_Page(request):
    _user = None
    template = loader.get_template('n6_Countries.html')
    context = {
        'Current_user':     _user,
        'Countries':             b06_Get_All_Countries(),
    }
    return HttpResponse(template.render(context, request))

def n7_Flights_Page(request):
    _user = None
    _user = request.session_user
    
    _my_flights = _all_flights = None
    if _user.Role == 3:
        _facade = Customer_Facade()
        _all_flights = _facade.d02_Get_All_Flights()
        _my_flights = _facade.i04_Get_My_Tickets(_user.id)
    elif _user.Role == 2:
        _facade = Airline_Facade()
        _all_flights = _facade.d02_Get_All_Flights()
        _my_flights = _facade.j05_Get_My_Flights(_user.id)
        
    
    template = loader.get_template('n7_Flights.html')
    context = {
        'Current_user':     _user,
        'All_Flights':      _all_flights,
        'My_Flights':       _my_flights,
    }
    return HttpResponse(template.render(context, request))

def n8_Tickets_Page(request):
   _user = None
   if 'user' in request.session:
        _userSession = request.session['user']
        _userList = list(serializers.deserialize("json", _userSession))
        _user = _userList[0].object
        
        if _user.Role.id != 1:
            return redirect('home')
    
        _user_facade = Administrator_Facade()
        if request.method == 'POST':
        
        # validate the CSRF token
            if not request.POST.get('csrfmiddlewaretoken'):
                return HttpResponseBadRequest('Missing CSRF token')
            template = loader.get_template('n8_Tickets.html')
            context = {
            'Current_user':     _user,
            'Tickets':             b08_Get_All_Tickets(),
             }
        return HttpResponse(template.render(context, request))