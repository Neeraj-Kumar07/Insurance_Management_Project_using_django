from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home_view, name='home'), # This is the missing link!
    path('aboutus', views.aboutus_view, name='aboutus'),
    path('contactus', views.contactus_view, name='contactus'),
    path('afterlogin', views.afterlogin_view, name='afterlogin'),
    path('admin-dashboard', views.admin_dashboard_view, name='admin-dashboard'),
    
]
