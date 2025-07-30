from django.urls import path, include
from . import views
from .views import LoginView

urlpatterns = [
    path('register', views.registration_view),
    path('login', LoginView.as_view(), name = "login")
]