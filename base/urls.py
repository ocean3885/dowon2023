from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('sub-intro/', views.sub_intro, name="sub-intro"),
    path('submit-jm/', views.submit_jm, name="submit-jm"),
    path('edit-submit/', views.edit_submit, name="edit-submit"),
    path('edit-submit-sj/', views.edit_submit_sj, name="edit-submit-sj"),
    path('submit-gm/', views.submit_gm, name="submit-gm"),
    path('submit-sj/', views.submit_sj, name="submit-sj"),
    path('find-submit/', views.find_submit, name="find-submit"),
    path('submit/delete/', views.delete_submit, name="delete-submit"),

]
