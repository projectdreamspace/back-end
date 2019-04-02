from django.urls import path
from . import views

urlpatterns = {
    path('', views.comingsoonpage, name='comingsoonpage'),
}