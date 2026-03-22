
#===========================================================================#
# from django.db import models
# from apps.customer.models import Customer

# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True)

#     def __str__(self):
#         return self.name

# class Policy(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     sum_assured = models.DecimalField(max_digits=12, decimal_places=2)
#     premium = models.DecimalField(max_digits=10, decimal_places=2)
#     tenure = models.IntegerField(help_text="Duration in years")
#     description = models.TextField()

#     def __str__(self):
#         return self.name

# class PolicyRecord(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
#     purchase_date = models.DateField(auto_now_add=True)
#     expiry_date = models.DateField()

#     def __str__(self):
#         return f"{self.customer.user.username} - {self.policy.name}"

# class Question(models.Model):
#     policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
#     question_text = models.TextField()

#     def __str__(self):
#         return self.question_text

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
#=====================================================================================#
