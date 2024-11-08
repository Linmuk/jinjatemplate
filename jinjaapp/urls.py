from django.urls import path
from jinjaapp import views



urlpatterns=[
    path('',views.home,name='home'),
    path('abt/',views.about,name='abt'),
    path('contact/',views.contact,name='contact'),
    path('servic',views.services,name='services'),
]