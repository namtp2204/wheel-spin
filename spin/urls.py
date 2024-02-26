from django.urls import path
from . import views

app_name = 'spin'

urlpatterns = [
    path("", views.navigation, name="navigation"),
    path('spin_form/', views.spin_form, name='spin_form'),
    
]
