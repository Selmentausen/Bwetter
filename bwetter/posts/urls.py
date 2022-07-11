from django.urls import path
from .views import dashboard

app_name = 'bwetter'

urlpatterns = [
    path('', dashboard, name='dashboard'),
]
