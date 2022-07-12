from django.urls import path
from .views import profile_list, profile

app_name = 'user_profile'

urlpatterns = [
    path('', profile_list, name='profile_list'),
    path('<int:pk>', profile, name='profile')
]
