from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from multiselectfield import MultiSelectField

# Create your models here.

class UserType(models.Model):
    Clients = 1
    Artists = 2
    TvChannel = 3
    RadioChannel = 4
    TYPE_CHOICES = (
        (Artists, 'Artists'),
        (Clients, 'Clients'),
        (TvChannel, 'TVChannel'),
        (RadioChannel, 'RadioChannel')
    )
    id = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, primary_key=True)
    
    def __str__(self):
        return self.get_id_display()

    
    

class UserRegistrationModel(models.Model):
    # Creating a one-to-one relationship with the User model in the database
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # Defining the view_artist permission
    class Meta:
         permissions=[("view_artist","View the artists")] 

    # Defining the create_project permission         
    class Meta:
        permissions=[("create_project","Create new project")]  

# Creating the Artist model
class Artist(models.Model):

    # Defining the name field
    name=models.CharField(max_length=120)

    # Defining the type field
    type=models.CharField(max_length=120)

    # Defining the active field with a default value of True
    active=models.BooleanField(default=True)
    
    # Defining the string representation of the model
    def __str__(self):
        return self.name

usertype = models.ManyToManyField(UserType)    

# Creating the Client model
class Client(models.Model):

    # Defining the name field
    name=models.CharField(max_length=120)

    # Defining the description field with blank and null values allowed
    description=models.TextField(blank=True,null=True)

    # Defining the active field with a default value of True
    active=models.BooleanField(default=True)
    
    # Defining the string representation of the model
    def __str__(self):
        return self.name        

# Creating the TvChannel model
class TvChannel(models.Model):

    # Defining the name field
    name=models.CharField(max_length=120)

    #Defining the description field with blank and null values allowed
    description=models.TextField(blank=True,null=True)

    #Defining the active field with a default value of true
    active=models.BooleanField(default=True)
    
    # Defining the string representation of the model
    def __str__(self):
        return self.name                

# Creating the RadioChannel model
class RadioChannel(models.Model):

    # Defining the name field
    name=models.CharField(max_length=120)

    #Defining the description field with blank and null values allowed
    description=models.TextField(blank=True,null=True)

    #Defining the active field with a default value of true
    active=models.BooleanField(default=True)
    
    # Defining the string representation of the model
    def __str__(self):
        return self.name  

              