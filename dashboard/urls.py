# dashboard/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.wallet_dashboard, name='wallet_dashboard'),
]

