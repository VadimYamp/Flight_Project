from django.contrib import admin
from django.urls import path, include
from App_A.views import *
from App_A.viewsAPI import *

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_home'),
    path('', Home, name='home'),
    path('X_Cust_Account/',
         X_Cust_Account,
         name='X_Cust_Account'),
    
    path('Y_Airline_Account/',
         Y_Airline_Account,
         name='Y_Airline_Account'),
    
    path('Z_Admin_Account/',
         Z_Admin_Account,
         name='Z_Admin_Account'),
    
    
    path('R_Cust_Registration/', R_Cust_Registration, name='R_Cust_Registration'),
    path('S_Airline_Registration/', S_Airline_Registration, name='S_Airline_Registration'),
    path('T_Admin_Registration/', T_Admin_Registration, name='T_Admin_Registration'),
    path('login/', Login, name="login"),
    path('logout/', Logout, name='logout'),
    path('test/', Test, name="test"),
    
    path('n1_Users_Page/',
         n1_Users_Page,
         name='n1_Users_Page'),
    
    path('n2_Customers_Page/',
         n2_Customers_Page,
         name='n2_Customers_Page'),
    
    path('n3_Airlines_Page/',
         n3_Airlines_Page,
         name='n3_Airlines_Page'),
    
    path('n4_Administrators_Page/',
         n4_Administrators_Page,
         name='n4_Administrators_Page'),
    
    path('n5_User_Roles_Page/',
         n5_User_Roles_Page,
         name='n5_User_Roles_Page'),
    
    path('n6_Countries_Page/',
         n6_Countries_Page,
         name='n6_Countries_Page'),
    
    path('n7_Flights_Page/',
         n7_Flights_Page,
         name='n7_Flights_Page'),
    
    path('n8_Tickets_Page/',
         n8_Tickets_Page,
         name='n8_Tickets_Page'),
    
    # API view html
    path('API_List/',
         API_List,
         name='API_List'),
    
    # API endpoints
    path('api/', include('App_A.urlsAPI'))
]
