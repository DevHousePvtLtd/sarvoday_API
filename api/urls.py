from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='api.home'),
    path('categories/', include('api.categories.urls')),
    path('rooms/', include('api.rooms.urls')),
]
