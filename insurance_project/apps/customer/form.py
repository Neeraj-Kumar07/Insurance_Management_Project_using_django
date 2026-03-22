from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    address = models.TextField()
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username
