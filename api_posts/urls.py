from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('<int:id>', views.put_delete_posts, name='put_delete_posts'),
    path('', views.get_post_posts, name='get_post_posts'),
]
