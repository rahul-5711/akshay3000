from django.urls import path  # importing the path funtion from Django's urls module.
from django.urls import reverse_lazy
from . import views
#from . import views

# Importing various views for handling authentication related funtionality from Django's auth.view module
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetDoneView, PasswordResetView,
    PasswordResetCompleteView, PasswordResetConfirmView,
    PasswordChangeView, PasswordChangeDoneView, PasswordResetDoneView
)

# Importing the views funtion for edit, dashboard, register.  
from .views import edit, dashboard, register                                     

# Defining the 'authapp' namespace for the urlpatterns in this module.
app_name = 'authapp'

# Defining the urlpatterns for this module.
urlpatterns = [

    # Mapping the URL path 'register/' to the register view function.
    path('register/', register, name='register'), 
    path('edit/', edit, name='edit'),
    path('dashboard/', dashboard, name='dashboard'),

    # Mapping the root URL path to the LoginView to provide Django's authentication framework
    # Using a custom login tempalte and the 'login' URL name.
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'), 
    path('logout/', LogoutView.as_view(template_name='authapp/logged_out.html'), name='logout'),
    path('password_change/', PasswordChangeView.as_view(
        template_name='authapp/password_change_form.html'), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='authapp/password_change_done.html'),
         name='password_change_done'),

    # Mapping the URL path 'passowrd_reset/' to the PasswordResetView to provide Django's authentication framework.
    # Using a custom password_reset_form template, a custom password_reset_email template, and the 'password_reset' URL name,
    # and specifying the success URL using the reverse_lazy function and the 'password_reset_done' URL name.     
    path('password_reset/', PasswordResetView.as_view(
        template_name='authapp/password_reset_form.html',
        email_template_name='authapp/password_reset_email.html',
        success_url=reverse_lazy('authapp:password_reset_done')), name='password_reset'),
    
    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='authapp/password_reset_done.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='authapp/password_reset_confirm.html',
        success_url=reverse_lazy('authapp:login')), name='password_reset_confirm'),

    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='authapp/password_reset_complete.html'), name='password_reset_complete'),  

          
     path('item/', views.item, name="item"),
]


