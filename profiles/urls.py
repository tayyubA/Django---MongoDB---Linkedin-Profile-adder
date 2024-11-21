from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_profile, name='create_profile'),
    path('list/', views.get_profiles, name='get_profiles'),
]
