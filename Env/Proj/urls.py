from django.contrib import admin
from django.urls import path, include

from App_A.urls import *

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    
    path('', include('App_A.urls')),
]
