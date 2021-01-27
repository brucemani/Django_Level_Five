from django.urls import path
from levelFiveApp import views

app_name = 'levelFiveApp'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
]
