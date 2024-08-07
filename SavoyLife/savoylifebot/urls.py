from django.urls import path
from . import views

app_name = 'savoylifebot'

urlpatterns = [
    path('', views.home_view, name='home'),  # Define the URL pattern for the root URL
    path('menu/', views.menu_view, name='menu'),
    path('chatbot/', views.chatbot_view, name='chatbot'),
]
