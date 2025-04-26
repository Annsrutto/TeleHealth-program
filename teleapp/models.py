from django.db import models

# Create your models here.

class Appointment(models.Model):
    """ This is the appointments table """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    date = models.DateField()
    department = models.CharField(max_length=20)
    doctor = models.CharField(max_length=15)
    message = models.TextField()
  
    def __str__(self):
        return self.name

class Contact(models.Model):
    """ This is the contacts table """
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name
