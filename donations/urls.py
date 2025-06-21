from django.urls import path
from donations import views

urlpatterns = [
    path('', views.donate_food, name='donate_food'),
    
]
