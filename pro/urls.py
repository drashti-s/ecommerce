from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.indexpage,name="indexpage"),
    path('manage/',views.manageproduct,name="manageproduct"),
    path('addproduct/',views.addproduct,name="addproduct"),
    path('singleproduct/',views.singleproduct,name="singleproduct"),
]