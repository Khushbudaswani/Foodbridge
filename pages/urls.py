from django.urls import path
from pages import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('donate-food/', views.donate_food, name='donate_food'),
    path('join-team/', views.join_team, name='join_team'),
    path('events/', views.events, name='events'),
    path('impact/', views.impact, name='impact'),
    path('partners/', views.partners, name='partners'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    
]
