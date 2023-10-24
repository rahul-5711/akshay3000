from django.contrib import admin
from .models import UserRegistrationModel
from .models import Artist
from .models import Client
from .models import TvChannel 
from .models import RadioChannel
from .models import UserType
from django import forms
from django.contrib.auth.models import User



# Register your models here.

admin.site.register(UserRegistrationModel) # Registering the UserRegistrationModel model
admin.site.register(Artist)                # Registering the Artist model.
admin.site.register(Client)                # Registering the Client model.
admin.site.register(TvChannel)             # Registering the TvChannel model.
admin.site.register(RadioChannel) 
admin.site.register(UserType)








