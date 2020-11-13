from django.urls import path
from . import views

app_name = 'frontend'
urlpatterns = [
    path('home/', views.index, name = 'index')
]