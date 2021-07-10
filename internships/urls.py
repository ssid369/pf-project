
from django.contrib import admin
from django.urls import path,include
import internships.views

urlpatterns = [
    path('',views.interns,name='intern'),
]
