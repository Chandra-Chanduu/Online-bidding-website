from django.urls import path
from . import views

urlpatterns=[
    path('register/',views.register_view,name='register_view'),
    path('profile/',views.profile_view,name='profile_view'),
    path('administration/',views.administration_view,name='administration_view'),
]