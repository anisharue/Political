from . import views
from django.urls import path

app_name = 'registration'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
]
