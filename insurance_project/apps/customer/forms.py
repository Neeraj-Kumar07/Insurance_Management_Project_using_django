#======================================================================================#

# from django.db import models
# from django.contrib.auth.models import User

# class Customer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
#     address = models.TextField()
#     mobile = models.CharField(max_length=15)

#     def __str__(self):
#         return self.user.username

from django import forms
from django.contrib.auth.models import User
from .models import Customer

class CustomerUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['address', 'mobile', 'profile_pic']
#========================================================================================#