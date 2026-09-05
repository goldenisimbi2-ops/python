from django.urls import path
from .import views

urlpatterns = [
    path('', views.My_appview, name='My_appview'),

]


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MyApp.urls')),
]