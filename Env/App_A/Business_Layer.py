from .models import *
from App_A.Data_Layer import *

# מחלקה כללית
class Base_Facade ():
    def __init__(self):
        pass

    # התחברות לחשבון
    def d01_Login(self, username, password):
        return c01_Get_User_By_Username(username, password)

    # רשימת כל הטיסות
    def d02_Get_All_Flights(self):
        return b07_Get_All_Flights()
    
    # טיסה לפי מספר סידורי
    def d03_Get_Flight_By_id(self,_id):
        return b14_Get_Flight_By_Id(id)
    
    # טיסה לפי נתונים:מדינת מקור,מדינת יעד ותאריך
    def d04_Get_Flights_By_Data(self,Origin_C_id, Dest_C_id, Date):
        return c05_Get_Flights_By_Data(Origin_C_id, Dest_C_id, Date)

    # רשימת כל החברות תעופה
    def d05_Get_All_Airlines(self):
        return b03_Get_All_Airline_Companies()

    # חברת תעופה לפי מספר סידורי
    def d06_Get_Airline_By_id(self,id):
        return b11_Get_Airline_By_Id()

    # חברת תעופה לפי מדינת הבית שלה
    def d07_Get_Airline_By_Data(self,Country):
        c10_Get_Airlines_By_Country(Country)

    # רשימת כל המדינות (תחנות)
    def d08_Get_All_Countries(self):
        return b06_Get_All_Countries()

    # מדינה לפי מספר סידורי
    def d09_Get_Country_By_id(self,id):
        return b13_Get_Country_By_Id(id)

    # יצירת משתמש חדש
    def d10_Create_New_User (self, User):
        pass

# מחלקת האורחים
class Anonymous_Facade(Base_Facade):

    # הרשמה
    def h02_Registration(self, request):
        # add validations of server side
        # for example that email have @ and .

        return self.d10_Create_New_User(None)

# מחלקת הלקוחות
class Customer_Facade(Base_Facade):
    
    #עדכון החשבון של הלקוח
    def i01_Update_Customer(self):
        pass

    # קניית כרטיס טיסה
    def i02_Add_Ticket (self,Flight_id):
        pass

    # ביטול כרטיס טיסה
    def i03_Remove_Ticket(self,Ticket_id):
        obj = b15_Get_Ticket_By_Id(Ticket_id)
        try:
            a05_Remove(obj.User)
            return True
        except Exception as e:
            #log.error()
            return False

    #רשימת הכרטיסי טיסה של הלקוח
    def i04_Get_My_Tickets (self,Cust_id):
        return c15_Get_Flights_By_Customer(id)

# מחלקת החברות-תעופה
class Airline_Facade(Base_Facade):
    # עדכון החשבון של החברת-תעופה
    def j01_Update_Airline (self,Airline_id):
        pass

    # פרסום טיסה חדשה
    def j02_Add_Flight (self,Origin_C_id,Dest_C_id,Begin_Date,Begin_Time,End_Date,End_Time,Q_Tickets):
        pass

    # עדכון טיסה קיימת
    def j03_Update_Flight(self, Flight_id):
        pass

    # ביטול טיסה
    def j04_Remove_Flight (self,Flight_id):
         obj = b14_Get_Flight_By_Id(Flight_id)
         try:
            a05_Remove(obj.User)
            return True
         except Exception as e:
            #log.error()
            return False

    # רשימת הטיסות של החברת-תעופה
    def j05_Get_My_Flights (self):
        return c06_Get_Flights_By_Airline_id(id)

# מחלקת המנהלים
class Administrator_Facade(Base_Facade):
    # צירוף לקוח חדש
    def k01_Add_Customer (self,Cust_First_Name,Cust_Last_Name,Cust_Address,Cust_Phone,Cust_Credit):
        pass

    # צירוף חברת-תעופה חדשה
    def k02_Add_Airline (self,Air_Name,Air_Country_id):
        pass

    # צירוף מנהל חדש
    def k03_Add_Administrator (self,Admin_First_Name,Admin_Last_Name):
        pass

    #מחיקת לקוח קיים
    def k04_Remove_User (self, _id, _role_id):
        if _role_id == 1:
            self.k07_Remove_Administrator(_id)
        elif _role_id == 2:
            self.k06_Remove_Airline(_id)
        elif _role_id == 3:
            self.k05_Remove_Customer(_id)
        else: # all other error roles from browser side
            raise "No such role exist."
        return True

    #מחיקת לקוח קיים
    def k05_Remove_Customer (self, Cust_id):
        obj = b10_Get_Customer_By_Id(Cust_id)
        try:
            a05_Remove(obj.User)
            return True
        except Exception as e:
            #log.error()
            return False
        

    #מחיקת חברת-תעופה קיימת
    def k06_Remove_Airline (self,Airline_id):
        obj = b11_Get_Airline_By_Id(Airline_id)
        try:
            a05_Remove(obj.User)
            return True
        except Exception as e:
            #log.error()
            return False

    # מחיקת מנהל קיים
    def k07_Remove_Administrator (self,Admin_id):
        obj = b12_Get_Administrator_By_Id(Admin_id)
        try:
            a05_Remove(obj.User)
            return True
        except Exception as e:
            #log.error()
            return False

    # רשימת כל המשתמשים
    def k08_Get_All_Users(self):
        return b01_Get_All_Users()
    
    # רשימת כל הלקוחות
    def k09_Get_All_Customers(self):
        return b02_Get_All_Customers()

    # רשימת כל החברות-תעופה
    def k10_Get_All_Airlines(self):
        return b03_Get_All_Airline_Companies()

    # רשימת כל המנהלים
    def k11_Get_All_Administrators (self):
        return b04_Get_All_Administrators() 
    
    # סיווג הרשאות במערכת
    def k12_Get_System_Roles (self):
        return b05_Get_All_User_Roles     
    
    # רשימת כל הכרטיסי-טיסה במערכת
    def k13_Get_All_Tickets(self):
        return b08_Get_All_Tickets()
    
     # רשימת כל המשתמשים
    def k14_Get_User_By_id(self,id):
        return b09_Get_User_By_id(id)
    
    # רשימת כל הלקוחות
    def k15_Get_Customer_By_id(self,id):
        return b10_Get_Customer_By_Id(id)

    # רשימת כל החברות-תעופה
    def k16_Get_Airline_By_id(self,id):
        return b11_Get_Airline_By_Id(id)

    # רשימת כל המנהלים
    def k17_Get_Administrator_By_id (self,id):
        return b12_Get_Administrator_By_Id(id)
    
    # כרטיס טיסה לפי מספר סידורי
    def k18_Get_Ticket_By_id(self,id):
        return b15_Get_Ticket_By_Id(id)