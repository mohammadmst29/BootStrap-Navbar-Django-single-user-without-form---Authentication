from django.contrib import admin
from django.urls import path

from .views import (
    homepage,
    signuppage,
    loginpage,
    logoutuser,

)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', homepage, name='homepage'),
    path('signupPage/', signuppage, name='signuppage'),  
    path('loginpage/', loginpage, name='loginpage'),
    path('logoutuser/', logoutuser, name='logoutuser'),
]
