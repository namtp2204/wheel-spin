
from django.urls import path
from .views import spin_form

urlpatterns = [
    path('spin-form/', spin_form, name='spin-form'),
    
]
