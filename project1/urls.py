from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('suahanghoa/<int:idhanghoa>/',views.suahanghoa,name='suahanghoa'),
    path('suahanghoa/',views.suahanghoa, name='themhanghoa'),
    path('dshanghoa/',views.dshanghoa,name='dshanghoa'),
]