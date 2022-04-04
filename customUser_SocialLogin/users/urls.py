from django.urls import include, path
from .views import *

urlpatterns = [
# path('auth/', include('rest_auth.urls')),    
# path('auth/register/', include('rest_auth.registration.urls'))
    path('google/', GoogleLogin.as_view(), name='google_login'),
    path('google/login/', google_login, name='google_login'),
    path('google/callback/', google_callback, name='google_callback'),  
    path('google/login/finish/', GoogleLogin.as_view(), name='google_login_todjango'),
    path('test/', test)
]