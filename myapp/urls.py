from django.contrib import admin
from django.urls import path, include  # Ensure include is imported
from myapp import views

from django.urls import path
from . import views  # Import views from the current directory

urlpatterns = [
    path('', views.home, name='home'),  # Home view from myapp
]