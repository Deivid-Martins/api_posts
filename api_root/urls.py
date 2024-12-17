from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('careers/', include('api_posts.urls'), name='api_posts_urls'),
]
