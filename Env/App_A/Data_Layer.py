from django import forms
from .models import *

#דף הבית
def Home_Page():
   return None



# טבלה שלמה מהבסיס-נתונים
def a01_Get_All(_model):
   return _model.objects.all()

# שורה אחת מתוך טבלה אחת לפי מספר סידורי
def a02_Get_by_id(_model, ID):
   return _model.objects.filter(id=ID)

# הוספה
def a03_Add(objToAdd):
    objToAdd.save()

# עדכון
def a04_Update(objToUpdate):
    objToUpdate.save()

# מחיקה
def a05_Remove(objToRemove):
    objToRemove.delete()

# הוספת רשימה
def a06_Add_All(ListToAdd):
   pass

# פונקציות לפי טבלאות
 #רשימת כל המשתמשים במערכת
def b01_Get_All_Users():
    Users = a01_Get_All(n1_Users)
    return Users

# רשימת כל הלקוחות במערכת
def b02_Get_All_Customers():
    Customers=a01_Get_All(n2_Customers)
    return Customers

# רשימת כל החברות-תעופה במערכת
def b03_Get_All_Airline_Companies():
    Airline_Companies = a01_Get_All(n3_Airline_Companies)
    return Airline_Companies

# רשימת כל המנהלים במערכת
def b04_Get_All_Administrators():
    Administrators = a01_Get_All(n4_Administrators)
    return Administrators

# דירוג ההרשאות
def b05_Get_All_User_Roles():
    User_Roles = a01_Get_All(n5_User_Roles)
    return User_Roles

# רשימת כל המדינות במערכת
def b06_Get_All_Countries():
    Countries = a01_Get_All(n6_Countries)
    return Countries

# רשימת כל הטיסות במערכת
def b07_Get_All_Flights():
    Flights = a01_Get_All(n7_Flights)
    return Flights

# רשימת כל הכרטיסי-טיסה במערכת
def b08_Get_All_Tickets():
    Tickets = a01_Get_All(n8_Tickets)
    return Tickets

# יבוא משתמש לפי מספר סידורי       
def b09_Get_User_By_id(_id):
    return n1_Users.objects.filter\
        (id=_id).first()

# יבוא לקוח לפי מספר סידורי 
def b10_Get_Customer_By_Id(_id):
    return n2_Customers.objects.filter\
        (id=_id).first()

# יבוא חברת-תעופה לפי מספר סידורי 
def b11_Get_Airline_By_Id(_id):
    return n3_Airline_Companies.objects.filter\
        (id=_id).first()
   
# יבוא מנהל לפי מספר סידורי  
def b12_Get_Administrator_By_Id(_id):
    return n4_Administrators.objects.filter\
        (id=_id).first()
        
# יבוא מדינה לפי מספר סידורי  
def b13_Get_Country_By_Id(_id):
    return n6_Countries.objects.filter\
        (id=_id).first()
        
# יבוא טיסה לפי מספר סידורי  
def b14_Get_Flight_By_Id(_id):
    return n7_Flights.objects.filter\
        (id=_id).first()
        
# יבוא כרטיס-טיסה לפי מספר סידורי  
def b15_Get_Ticket_By_Id(_id):
    return n8_Tickets.objects.filter\
        (id=_id).first()
        
# פונקציות מתקדמות
# יבוא משתמש לפי השם משתמש
def c01_Get_User_By_Username(_Username, _Password):
    return n1_Users.objects.filter\
        (Name=_Username, Password=_Password)

# יבוא לקוח לפי השם משתמש
def c02_Get_Customer_By_Username(_Username):
    return n2_Customers.objects.filter\
        (User__Name=_Username).first()
        
# יבוא חברת-תעופה לפי השם משתמש
def c03_Get_Airline_By_Username(_Username):
    return n3_Airline_Companies.objects.filter\
        (User__Name=_Username)
        
# יבוא מנהל לפי השם משתמש
def c04_Get_Administrator_By_Username(_Username):
    return n4_Administrators.objects.filter\
        (User__Name=_Username)
      
# יבוא טיסות לפי נתונים:מדינת מקור,מדינת יעד וזמן
def c05_Get_Flights_By_Data(_Origin_C_id, _Dest_C_id, _Date):
    return n7_Flights.objects.filter\
        (Origin_id=_Origin_C_id,Dest_id=_Dest_C_id,Begin_Date=_Date)

#יבוא טיסות לפי מספר חברת-תעופה 
def c06_Get_Flights_By_Airline_id(_Airline_id):
    return n7_Flights.objects.filter\
        (Company_id=_Airline_id)

# יבוא טיסות שממריאות ממדינה מסוימת
def c07_Get_Departure_Flights(_country_id):
    return n7_Flights.objects.filter\
        (Origin_id=_country_id)

# יבוא טיסות שנוחתות במדינה מסוימת
def c08_Get_Arrival_Flights(_country_id):
    return n7_Flights.objects.filter\
        (Dest_id=_country_id)

# יבוא כרטיסי טיסה ששייכים ללקוח מסוים
def c09_Get_Tickets_By_Customer(_Cust_id):
    return n8_Tickets.objects.filter\
        (Cust_id=_Cust_id)

# יבוא כל החברות-תעופה ששוכנות במדינה מסוימת
def c10_Get_Airlines_By_Country(_Country):
    return n3_Airline_Companies.objects.filter\
        (Country__Name=_Country)
# יבוא טיסות שממריאות ממדינה מסוימת
def c11_Get_Flights_By_Origin_Country_id(_Origin_C_id):
    return n7_Flights.objects.filter \
        (Origin_id=_Origin_C_id)

# יבוא טיסות שנוחתות במדינה מסוימת
def c12_Get_Flights_By_Dest_Country_id(_Dest_C_id):
    return n7_Flights.objects.filter \
        (Dest_id=_Dest_C_id)

# יבוא כל הטיסות שממריאות בתאריך מסוים
def c13_Get_Flights_By_Takeoff_Date(_Takeoff_Date):
    return n7_Flights.objects.filter \
        (Begin_Date=_Takeoff_Date)

# יבוא כל הטיסות שנוחתות בתאריך מסוים
def c14_Get_Flights_By_Landing_Date(_Landing_Date):
    return n7_Flights.objects.filter \
        (End_Date=_Landing_Date)

# יבוא כל הטיסות של לקוח מסוים
def c15_Get_Flights_By_Customer(_Cust_id):
    return n8_Tickets.Flight.objects.filter \
        (Customer__id=_Cust_id)

# def formfield_for_dbfield(db_field, **kwargs):
#     if db_field.name == "Role":
#         return 1
#     return db_field.formfield(**kwargs)

# פונקציות להרשמה והתחברות זמניים
class RegistrationForm(forms.ModelForm):   
    Password = forms.CharField(widget=forms.PasswordInput, label='סיסמא') 
    Email = forms.CharField(widget=forms.EmailInput, label="דואר") 

    class Meta:
        model = n1_Users
        fields = ['Name']
        labels = {'Name': 'שם משתמש'}
        model = n2_Customers
        fields = ['First_Name', 'Last_Name', 'Address','Phone','Credit']
        labels = {'First_Name': 'שם-פרטי',
                  'Last_Name': 'שם משפחה',
                  'Address':'כתובת',
                  'Phone':'טלפון',
                  'Credit':'אשראי'}
        #exclude = ['Role']
        #formfield_callback = formfield_for_dbfield     
class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = n1_Users
        fields = ['Name', 'Password']
        