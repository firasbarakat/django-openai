from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('prompt', views.postData)
]