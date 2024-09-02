from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),  # Include dashboard URLs
    path('', lambda request: redirect('wallet_dashboard', permanent=False)),  # Redirect root to the dashboard
]
