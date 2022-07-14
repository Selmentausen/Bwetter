from django.urls import path
from .views import dashboard, new_post

app_name = 'posts'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('new_post/', new_post, name='new_post')
]
