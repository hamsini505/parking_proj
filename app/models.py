from django.db import models

class signin(models.Model):
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length = 20)

    #def __str__(self) :
     #   return self.email

class signup(models.Model):
    username = models.CharField(max_length = 30)
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length = 20)
    confirm_password = models.CharField(max_length = 20)
    date_birth = models.DateField(max_length = 10)

    #def __str__(self) :
      #  return self.username

class forgot(models.Model):
    username = models.CharField(max_length = 30)
    email = models.CharField(max_length = 50)
    date_birth = models.DateField(max_length = 10)
    new_password = models.CharField(max_length = 20)
    confirm_new_password = models.CharField(max_length = 20)

    #def __str__(self) :
     #   return self.username

class details(models.Model):
    vehicle_type = models.CharField(max_length = 5)
    vehicle_num = models.CharField(max_length = 10)
    slot_time = models.TimeField(max_length = 15)
    slot_date = models.DateField(max_length = 10)

#    def __str__(self) :
 #       return self.vehicle_type




