
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import include
from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns
#from django.conf.global_settings import LANGUAGE
 
urlpatterns = [
   # path('', include('authapp.urls', namespace='authapp')),
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
  
]

urlpatterns += i18n_patterns (
    path('', include('authapp.urls', namespace='authapp'))
)
