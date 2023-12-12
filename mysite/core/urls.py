# urls.py

from django.urls import path
from . import views

urlpatterns = [
    # path('register/', views.register, name='api-register'),
    path('contact/', views.contact, name='api-contact'),
]
