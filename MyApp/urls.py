from django.urls import path
from .import views

urlpatterns = [
    path('', views.My_appview, name='My_appview'),
    path('Profiles/', views.Profile_list, name='Profile_list'),
    path('Profiles/<int:pk>/', views.Profile_detail, name='Profile_detail'),

]