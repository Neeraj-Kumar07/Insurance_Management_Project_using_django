from django.urls import path
from django.contrib.auth.views import LoginView # Add this import
from . import views

urlpatterns = [ 
    path('', views.home_view, name='home'),
    path('aboutus', views.aboutus_view, name='aboutus'),
    path('contactus', views.contactus_view, name='contactus'),
    path('afterlogin', views.afterlogin_view, name='afterlogin'),
    path('admin-dashboard', views.admin_dashboard_view, name='admin-dashboard'),
    
    
    path('adminlogin', LoginView.as_view(template_name='insurance/adminlogin.html'), name='adminlogin/'),
    path('adminclick', views.adminclick_view, name='adminclick'),
]