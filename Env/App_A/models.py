from django.db import models
from django.utils import timezone
import datetime as datetime

class n1_Users(models.Model):
   Name     = models.CharField(max_length=30)
   Password = models.CharField(max_length=30)
   Email    = models.CharField(max_length=30)
   Role     = models.ForeignKey("n5_User_Roles", on_delete=models.CASCADE, default=3)

class n2_Customers(models.Model):
   First_Name = models.CharField(max_length=30)
   Last_Name  = models.CharField(max_length=30)
   Address    = models.CharField(max_length=30)
   Phone      = models.CharField(max_length=11)
   Credit     = models.CharField(max_length=16)
   User       = models.ForeignKey("n1_Users", on_delete=models.CASCADE)

class n3_Airline_Companies(models.Model):
   Name     = models.CharField(max_length=30)
   Country  = models.ForeignKey("n6_Countries", on_delete=models.CASCADE)
   User     = models.ForeignKey("n1_Users", on_delete=models.CASCADE)

class n4_Administrators(models.Model):
   First_Name = models.CharField(max_length=30)
   Last_Name  = models.CharField(max_length=30)
   User       = models.ForeignKey("n1_Users", on_delete=models.CASCADE)

class n5_User_Roles(models.Model):
   Name     = models.CharField(max_length=30)

class n6_Countries(models.Model):
   Name     = models.CharField(max_length=30)

class n7_Flights(models.Model):
   Company  = models.ForeignKey("n3_Airline_Companies", on_delete=models.CASCADE)
   Origin   = models.ForeignKey("n6_Countries", on_delete=models.CASCADE,related_name='Origin_Countries')
   Dest     = models.ForeignKey("n6_Countries", on_delete=models.CASCADE,related_name='Dest_Countries')
   Begin_DateTime = models.DateTimeField(default=datetime.datetime.now, blank=True)
   End_DateTime   = models.DateTimeField(default=datetime.datetime.now, blank=True)
   Q_Tickets      = models.IntegerField(default=0)

class n8_Tickets(models.Model):
   Flight  = models.ForeignKey("n7_Flights", on_delete=models.CASCADE)
   Cust    = models.ForeignKey("n2_Customers", on_delete=models.CASCADE)
