from django.urls import path, include
from home.views import *

urlpatterns = [
    path('', login_server),
    path('index/', index),
    path('register/', register),
]
