from django.urls import path, include
from .views import profile_list, profile, register

app_name = 'user_profile'

urlpatterns = [
    path('', profile_list, name='profile_list'),
    path('<int:pk>', profile, name='profile'),
    path('register', register, name='register')
]
