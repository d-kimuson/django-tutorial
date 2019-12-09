from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('message/<int:pk>', views.message, name='index'),
]
