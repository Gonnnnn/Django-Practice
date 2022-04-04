from django.urls import path, include

import sociallogin
from .views import *

urlpatterns = [
    path('sociallogin/', include('allauth.urls')),
    path('', sociallogin, name='sociallogin'),
]
