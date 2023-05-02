from django.contrib import admin
from django.urls import path, include
from App_A.views import *
from App_A.viewsAPI import *

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_home'),
    path('', Home, name='home'),
    
    
    path('Cust_Account/', X_Cust_Account, name='Cust_Account'),
    path('Airline_Account/', Y_Airline_Account, name='Airline_Account'),
    path('Admin_Account/', Z_Admin_Account, name='Admin_Account'),
    
    
    path('R_Cust_Registration/', R_Cust_Registration, name='R_Cust_Registration'),
    path('S_Airline_Registration/', S_Airline_Registration, name='S_Airline_Registration'),
    path('T_Admin_Registration/', T_Admin_Registration, name='T_Admin_Registration'),
    path('login/', Login, name="login"),
    path('logout/', Logout, name='logout'),
    path('test/', Test, name="test"),
    
    path('n1/', n1, name='n1'),
    path('n2/', n2, name='n2'),
    path('n3/', n3, name='n3'),
    path('n4/', n4, name='n4'),
    path('n5/', n5, name='n5'),
    path('n6/', n6, name='n6'),
    path('n7/', n7, name='n7'),
    path('n8/', n8, name='n8'),
    
    # API view html
    path('c2_API/', c2, name='c2'),
    
    # API endpoints
    path('api/', include('App_A.urlsAPI'))
]
