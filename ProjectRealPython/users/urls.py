from users.views import dashboard
from django.urls import path, include , re_path
from users import views


urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    ]