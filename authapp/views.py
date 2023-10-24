# Import necessary module
from django.http import request 
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistration, UserEditForm
from django.conf import settings
from django.core.mail import send_mail


# Create your views here

@login_required
def dashboard(request):

    # Create context dictionary to pass variables to the template
    context = {
        "welcome": "Welcome to your dashboard"
    }

    # Render the dashboard.html template with context
    return render(request, 'authapp/dashboard.html', context=context)

# Function to handle registration 
def register(request):

    # Check if the request is a POST request
    if request.method == 'POST':

        # Create UserRegistration form object with post data.
        form = UserRegistration(request.POST or None)

        # Check if form is valid.
        if form.is_valid():

            # Create a new_user object without committing to database. 
            new_user = form.save(commit=False)

            # Set the user password using the cleaned_data from the form. 
            new_user.set_password(
                form.cleaned_data.get('password')
            )

            # save the user to the database.
            new_user.save()

            # Render the register_done.html template.
            return render(request, 'authapp/register_done.html')
    else:

        # If the request is not a POST request, create a new UserRegistration form object
        form = UserRegistration()
    
    # Create a context dictionary to pass variables to the template.
    context = {
        "form": form
    }
     
    # Render the register.html template with context. 
    return render(request, 'authapp/register.html', context=context)


@login_required
# Function to handle edit.
def edit(request):

    # Check if the request is a POST request.
    if request.method == 'POST':

        # Create UserRegistration form object with post data and current user instance
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        # Check if the form is valid.                         
        if user_form.is_valid():
            user_form.save()
    else:

        # if request is not POST , Create a new UserEditForm without current user instance
        user_form = UserEditForm(instance=request.user)

    # Create a context dictionary to pass variables to the template.    
    context = {
        'form': user_form,
    }

    # Render the edit.html template with context. 
    return render(request, 'authapp/edit.html', context=context)

from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
from django.utils import translation

def item(request):
    trans = translate(language='fr')
    return render(request, 'item.html', {'trans':trans})


def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = gettext('hello')
    finally:
        activate(cur_language)
    return text        



