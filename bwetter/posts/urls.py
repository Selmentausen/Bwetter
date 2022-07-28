from django.urls import path
from .views import dashboard, new_post, post_index, comment_add, comment_delete

app_name = 'posts'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('new_post/', new_post, name='new_post'),
    path('<int:pk>', post_index, name='post_index'),
    path('<int:post_pk>/comment_add', comment_add, name='comment_add'),
    path('<int:post_pk>/comment_delete/<int:comment_pk>', comment_delete, name='comment_delete'),
]
