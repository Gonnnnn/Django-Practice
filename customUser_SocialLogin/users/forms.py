# from django import forms
# from django.contrib.auth.forms import UserChangeForm,         UserCreationForm 
# # from django.contrib.auth import get_user_model
# from .models import User
# # admin에 넣어줄건데 이미 해놔서 쓸필요가 없을거같긴함

# # User = get_user_model()
# class CustomUserCreationForm(UserCreationForm):    
#     class Meta:        
#         model = User        
#         fields = ('email', 'name', 'is_staff', 'is_superuser')  
# class CustomUserChangeForm(UserChangeForm):    
#     class Meta:        
#         model = User        
#         fields = UserChangeForm.Meta.fields