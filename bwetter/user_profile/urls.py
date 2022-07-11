from django.urls import path
from .views import profile_list

app_name = 'profile_list'

urlpatterns = [
    path('', profile_list, name='profile_list'),
]