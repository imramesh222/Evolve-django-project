from django.urls import path

from .views import *

urlpatterns = [
    path('register/',register),
    path('userlogin/',userLogin),
    path('userlogout/',userLogout),
]
