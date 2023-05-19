from django.urls import path
from . import views

app_name = 'webapp'

urlpatterns = [
    path('', views.home),
    path('about/', views.about, name='about'),
    path('volunteer/', views.volunteer),
    path('contact/', views.contact),
]
