from django.urls import path
from . import views



urlpatterns = [
    # path("", views.navigation, name="navigation"),
    path('spin_form/', views.spin_form, name='spin_form'),
    path('spin_wheel/<str:spin_code>/', views.spin_wheel, name='spin_wheel'),
    # path('show_spin_codes/', views.show_spin_codes, name='show_spin_codes'), 
]
