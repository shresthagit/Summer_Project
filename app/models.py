from pickle import FALSE, TRUE
from unittest.util import _MAX_LENGTH
from django.db import models


# Create your models here.
class service(models.Model):
    service_name = models.CharField(max_length=100)
    charge= models.BigIntegerField()

    def __str__(self):
        return str(self.service_name)

# class Admin(models.Model):
#     username = models.CharField(max_length=100)
#    # password= models.Textfield(max_length=100)
#     email= models.CharField(max_length=100)
#     phone= models.BigIntegerField()
#     address = models.CharField(max_length=100)

#     def __str__(self):
#         return str(self.username)

# class Doctor(models.Model):
#     doctor_name = models.CharField(max_length=100)
#     doctor_info= models.CharField(max_length=50)   
#     Charge= models.BigIntegerField()

#     def __str__(self):
#         return str(self.doctor_name)

class Customer(models.Model):
    cus_username = models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    phone= models.BigIntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return str(self.cus_username)

class Payment(models.Model):
    payment_name = models.CharField(max_length=100)
    payment_method= models.CharField(max_length=50)   
    payment_number= models.BigIntegerField()
    payment_date =models.IntegerField()
    transaction_id=models.IntegerField(null=TRUE)

    def __str__(self):
        return str(self.payment_name)

class Appointment(models.Model):
    appointment_name=models.TextField(max_length=20)
    appointment_date=models.CharField(max_length=100)
    appointment_time=models.CharField(max_length=100)
    appointment_service=models.TextField()
    appointment_feedback=models.TextField(null=TRUE)

    def __str__(self):
        return str(self.appointment_name)



class User(models.Model):
    username = models.TextField()
    email = models.EmailField()
    password = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    contact = models.IntegerField()
    address = models.CharField(max_length=100)
    
    def __str__(self):
     return str(self.fullname)

class report(models.Model):
    patient_name=models.TextField()
    address=models.CharField(max_length=100)
    contact=models.IntegerField()
    doctor=models.TextField()
    detail=models.TextField()
    treatment=models.TextField()
    recommendation=models.TextField()

    def __str__(self):
        return str(self.patient_name)


