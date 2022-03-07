from django.urls import path
from .views import *

urlpatterns = [
    path('', BookingList.as_view()),
    path('<int:pk>/', BookingDetail.as_view()),
]
