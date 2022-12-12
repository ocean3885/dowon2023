from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('sub-intro/', views.sub_intro, name="sub-intro"),
    path('submit-jm/', views.submit_jm, name="submit-jm"),
    path('submit-jm/edit/<str:pk>/', views.edit_submit_jm, name="edit-submit-jm"),
    path('find-submit/', views.find_submit, name="find-submit"),
]
