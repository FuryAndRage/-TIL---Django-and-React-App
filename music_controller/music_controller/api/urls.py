from django.urls import path
from . import views
app_name = 'api'

urlpatterns = [
    path('', views.RoomView.as_view(), name = 'view')
]