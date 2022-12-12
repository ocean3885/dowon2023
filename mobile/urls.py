from django.urls import path,include
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('', views.m_Home, name="m-home"),
    path('m-jm-submit/', views.M_Jm_Submit, name="m-jm-submit"),
]
