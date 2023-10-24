from django.contrib.auth.models import User
from django import forms
# from .models import Profile
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from .models import UserRegistrationModel
from django.contrib.auth.forms import PasswordResetForm


class UserRegistration(forms.ModelForm):
    # This form field is for the password
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    # This form field is for confirming the password
    password2 = forms.CharField(
        label='Repeat Password', widget=forms.PasswordInput)

    # This is the Meta class for the form, it defines the model and the fields that should be displayed in the form
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

        # This method is used for password confirmation validation
        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Passwords don\'t match.')
            return cd['password2']

# This is a form for editing the user's information
class UserEditForm(forms.ModelForm):

    # This is the Meta class for the form, it defines the model and the fields that should be displayed in the form
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


        



 


      


