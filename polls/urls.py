from django.urls import path
from .views import *

urlpatterns = [
    path('test/', test, name='index'),
    path('', index, name='index'),
    path('get/<int:question_id>/', get, name='get'),
]
