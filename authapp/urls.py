from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_render, name="login_render"),
    path('company-registration/', views.company_registration, name="Company Registration")
]
