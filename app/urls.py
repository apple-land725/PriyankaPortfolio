from django.urls import path, include
from .import views
# from django import forms



urlpatterns = [
    path("",views.IndexPageView,name="indexpage"),
    path('contact/', views.ContactView, name='contact'),
    path('Contact/submit', views.InsertData, name='contact_submit'),
    path('contact/', views.ThankView, name='thank'),
   
]
