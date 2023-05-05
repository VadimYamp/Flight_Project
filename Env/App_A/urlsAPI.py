from django.contrib import admin
from django.urls import path
from App_A.viewsAPI import *

urlpatterns = [
    path('API_List/',
          API_List,          
          name='API_List'),
      
    path('API_01_GetAllUsers/',
          API_01_GetAllUsers,          
          name='API_01_GetAllUsers'),
    
    path('API_02_GetAllCustomers/',  
          API_02_GetAllCustomers, 
          name='API_02_GetAllCustomers'),
    
    path('API_03_GetAllAirlines/', 
          API_03_GetAllAirlines,     
          name='API_03_GetAllAirlines'),
    
    path('API_04_GetAllAdministrators/',
          API_04_GetAllAdministrators,
          name='API_04_GetAllAdministrators'),
    
    path('API_05_GetAllUserRoles/',
          API_05_GetAllUserRoles,
          name='API_05_GetAllUserRoles'),
    
    path('API_06_GetAllCountries/',
          API_06_GetAllCountries,      
          name='API_06_GetAllCountries'),
    
    path('API_07_GetAllFlights/',
          API_07_GetAllFlights, 
          name='API_07_GetAllFlights'),
    
    path('API_08_GetAllTickets/',
          API_08_GetAllTickets,     
          name='API_08_GetAllTickets'),
    
    
    
    path('API_09_GetUserById/',
          API_09_GetUserById, 
          name='API_09_GetUserById'),
    
    path('API_10_GetCustomerById/',
          API_10_GetCustomerById,
          name='API_10_GetCustomerById'),
    
    path('API_11_GetAirlineById/',
          API_11_GetAirlineById,
          name='API_11_GetAirlineById'),
    
    path('API_12_GetAdministratorById/',
          API_12_GetAdministratorById, 
          name='API_12_GetAdministratorById'),
    
    path('API_13_GetCountryById/',
          API_13_GetCountryById,
          name='API_13_GetCountryById'),
    
    path('API_14_GetFlightById/',
          API_14_GetFlightById,   
          name='API_14_GetFlightById'),
    
    path('API_15_GetTicketById/',
          API_15_GetTicketById,     
          name='API_15_GetTicketById'),
    
    path('RemoveCustomer/',
          RemoveCustomer,     
          name='RemoveCustomer'),
]