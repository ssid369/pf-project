
from django.contrib import admin
from django.urls import path,include
from. import views

urlpatterns = [
    path('',views.internsh,name='intern'),
    path('<int:intern_id>/',views.details,name='detail'),
]
