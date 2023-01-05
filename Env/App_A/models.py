from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class n1_Users(models.Model):
   Name     = models.CharField(max_length=30)
   Password = models.CharField(max_length=30)
   Email    = models.CharField(max_length=30)
   Role     = models.IntegerField(default=0)

class n2_Customers(models.Model):
   First_Name = models.CharField(max_length=30)
   Last_Name  = models.CharField(max_length=30)
   Address    = models.CharField(max_length=30)
   Phone      = models.CharField(max_length=11)
   Credit     = models.CharField(max_length=16)
   Phone      = models.CharField(max_length=11)
   User_ID    = models.IntegerField(default=0)

class n3_Airline_Companies(models.Model):
   Name     = models.CharField(max_length=30)
   Country_ID = models.IntegerField(default=0)
   User_ID    = models.IntegerField(default=0)

class n4_Administrators(models.Model):
   First_Name = models.CharField(max_length=30)
   Last_Name  = models.CharField(max_length=30)
   User_ID    = models.IntegerField(default=0)

class n5_User_Roles(models.Model):
   Name     = models.CharField(max_length=30)



class n6_Countries(models.Model):
   Name     = models.CharField(max_length=30)

class n7_Flights(models.Model):
   Company_ID = models.IntegerField(default=0)
   Origin_ID  = models.IntegerField(default=0)
   Dest_ID    = models.IntegerField(default=0)
   Begin      = models.DateTimeField()
   End        = models.DateTimeField()
   Q_Tickets  = models.IntegerField(default=0)


class n8_Tickets(models.Model):
   Flight_ID = models.IntegerField(default=0)
   Cust_ID   = models.IntegerField(default=0)

