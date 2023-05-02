import datetime
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.template import loader
from django.core import serializers
from App_A.Data_Layer import * 
from App_A.Business_Layer import *


def c2(request):
    _user = None
    if 'user' in request.session:
        _userSession = request.session['user']
        _userList = list(serializers.deserialize("json", _userSession))
        _user = _userList[0].object
        
        if _user.Role.id != 1:
            return redirect('home')
        
    template = loader.get_template('API.html')
    context = {
        'Current_user':     _user,
    }
    return HttpResponse(template.render(context, request))

#1.
@api_view(['GET'])
def API_01_GetAllUsers(request):
    user = None
    if 'user' in request.session:
        userSession = request.session['user']
        userList = list(serializers.deserialize("json", userSession))
        user = userList[0].object
        
        if user.Role.id != 1:
            return redirect('home')
    
    user_facade = Administrator_Facade()
    items = user_facade.k08_Get_All_Users()
    data = {'items': list(items.values())} 
    return JsonResponse(data)

#2.
@api_view(['GET'])
def API_02_GetAllCustomers(request):
    user = None
    if 'user' in request.session:
        userSession = request.session['user']
        userList = list(serializers.deserialize("json", userSession))
        user = userList[0].object
        
        if user.Role.id != 1:
            return redirect('home')
    
    user_facade = Administrator_Facade()
    items = user_facade.k09_Get_All_Customers()
    data = {'items': list(items.values())} 
    return JsonResponse(data)

#3.
@api_view(['GET'])
def API_03_GetAllAirlines(request):
    user = None
    if 'user' in request.session:
        userSession = request.session['user']
        userList = list(serializers.deserialize("json", userSession))
        user = userList[0].object
        
        if user.Role.id != 1:
            return redirect('home')
    
    user_facade = Administrator_Facade()
    items = user_facade.k10_Get_All_Airlines()
    data = {'items': list(items.values())} 
    return JsonResponse(data)

#4.
@api_view(['GET'])
def API_04_GetAllAdministrators(request):
    user = None
    if 'user' in request.session:
        userSession = request.session['user']
        userList = list(serializers.deserialize("json", userSession))
        user = userList[0].object
        
        if user.Role.id != 1:
            return redirect('home')
    
    user_facade = Administrator_Facade()
    items = user_facade.k11_Get_All_Administrators()
    data = {'items': list(items.values())} 
    return JsonResponse(data)

#5.
def API_05_GetAllUserRoles(request):
    user = None
    if 'user' in request.session:
        userSession = request.session['user']
        userList = list(serializers.deserialize("json", userSession))
        user = userList[0].object
        
        if user.Role.id != 1:
            return redirect('home')
    
    user_facade = Administrator_Facade()
    items = user_facade.k12_Get_System_Roles()
    data = {'items': list(items.values())} 
    return JsonResponse(data)

#6.
def API_06_GetAllCountries(request):
    user = None
    if 'user' in request.session:
        userSession = request.session['user']
        userList = list(serializers.deserialize("json", userSession))
        user = userList[0].object
        
        if user.Role.id != 1:
            return redirect('home')
    
    user_facade = Administrator_Facade()
    items = user_facade.d08_Get_All_Countries()
    data = {'items': list(items.values())} 
    return JsonResponse(data)

#7.
def API_07_GetAllFlights(request):
    user = None
    if 'user' in request.session:
        userSession = request.session['user']
        userList = list(serializers.deserialize("json", userSession))
        user = userList[0].object
        
        if user.Role.id != 1:
            return redirect('home')
    
    user_facade = Administrator_Facade()
    items = user_facade.d02_Get_All_Flights()
    data = {'items': list(items.values())} 
    return JsonResponse(data)

#8.
def API_08_GetAllTickets(request):
    user = None
    if 'user' in request.session:
        userSession = request.session['user']
        userList = list(serializers.deserialize("json", userSession))
        user = userList[0].object
        
        if user.Role.id != 1:
            return redirect('home')
    
    user_facade = Administrator_Facade()
    items = user_facade.k13_Get_All_Tickets()
    data = {'items': list(items.values())} 
    return JsonResponse(data)



#9.
@api_view(['POST'])
def API_09_GetUserById(request):
    user = None
    if 'user' in request.session:
        userSession = request.session['user']
        userList = list(serializers.deserialize("json", userSession))
        user = userList[0].object
        
        if user.Role.id != 1:
            return redirect('home')
    
    data = request.data
    user_id = data.get('user_id')
    
    user_facade = Administrator_Facade()
    isSuccess = user_facade.k14_Get_User_By_id(user_id)
    data = {'Yes': isSuccess} 
    return JsonResponse(data)

#10.
@api_view(['POST'])
def API_10_GetCustomerById(request):
    user = None
    if 'user' in request.session:
        userSession = request.session['user']
        userList = list(serializers.deserialize("json", userSession))
        user = userList[0].object
        
        if user.Role.id != 1:
            return redirect('home')
    
    data = request.data
    cust_id = data.get('cust_id')
    
    user_facade = Administrator_Facade()
    isSuccess = user_facade.k15_Get_Customer_By_id(cust_id)
    data = {'Yes': isSuccess} 
    return JsonResponse(data)

#11.
@api_view(['POST'])
def API_11_GetAirlineById(request):
    user = None
    if 'user' in request.session:
        userSession = request.session['user']
        userList = list(serializers.deserialize("json", userSession))
        user = userList[0].object
        
        if user.Role.id != 1:
            return redirect('home')
    
    data = request.data
    airline_id = data.get('airline_id')
    
    user_facade = Administrator_Facade()
    isSuccess = user_facade.k16_Get_Airline_By_id(airline_id)
    data = {'Yes': isSuccess} 
    return JsonResponse(data)

#12.
@api_view(['POST'])
def API_12_GetAdministratorById(request):
    user = None
    if 'user' in request.session:
        userSession = request.session['user']
        userList = list(serializers.deserialize("json", userSession))
        user = userList[0].object
        
        if user.Role.id != 1:
            return redirect('home')
    
    data = request.data
    admin_id = data.get('admin_id')
    
    user_facade = Administrator_Facade()
    isSuccess = user_facade.k17_Get_Administrator_By_id(admin_id)
    data = {'Yes': isSuccess} 
    return JsonResponse(data)

#13.
@api_view(['POST'])
def API_13_GetCountryById(request):
    user = None
    if 'user' in request.session:
        userSession = request.session['user']
        userList = list(serializers.deserialize("json", userSession))
        user = userList[0].object
        
        if user.Role.id != 1:
            return redirect('home')
    
    data = request.data
    country_id = data.get('country_id')
    
    user_facade = Administrator_Facade()
    isSuccess = user_facade.d09_Get_Country_By_id(country_id)
    data = {'Yes': isSuccess} 
    return JsonResponse(data)

#14.
@api_view(['POST'])
def API_14_GetFlightById(request):
    user = None
    if 'user' in request.session:
        userSession = request.session['user']
        userList = list(serializers.deserialize("json", userSession))
        user = userList[0].object
        
        if user.Role.id != 1:
            return redirect('home')
    
    data = request.data
    flight_id = data.get('flight_id')
    
    user_facade = Administrator_Facade()
    isSuccess = user_facade.d03_Get_Flight_By_id(flight_id)
    data = {'Yes': isSuccess} 
    return JsonResponse(data)

#15.
@api_view(['POST'])
def API_15_GetTicketById(request):
    user = None
    if 'user' in request.session:
        userSession = request.session['user']
        userList = list(serializers.deserialize("json", userSession))
        user = userList[0].object
        
        if user.Role.id != 1:
            return redirect('home')
    
    data = request.data
    ticket_id = data.get('ticket_id')
    
    user_facade = Administrator_Facade()
    isSuccess = user_facade.k18_Get_Ticket_By_id(ticket_id)
    data = {'Yes': isSuccess} 
    return JsonResponse(data)

@api_view(['POST'])
def RemoveCustomer(request):
    user = None
    if 'user' in request.session:
        userSession = request.session['user']
        userList = list(serializers.deserialize("json", userSession))
        user = userList[0].object
        
        if user.Role.id != 1:
            return redirect('home')
    
    data = request.data
    cust_id = data.get('cust_id')
    
    user_facade = Administrator_Facade()
    isSuccess = user_facade.k05_Remove_Customer(cust_id)
    data = {'Yes': isSuccess} 
    return JsonResponse(data)
