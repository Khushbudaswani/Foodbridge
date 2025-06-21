from django.urls import path
from volunteers import views

urlpatterns = [
    path('', views.join_team, name='join_team'),
]
