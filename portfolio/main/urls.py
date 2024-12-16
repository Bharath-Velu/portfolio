from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home , name='home'),
    path('conact/' , views.contact , name='contact'),
    path('about/', views.about, name='about'),
    path('thanks/' , views.thanks , name='thanks')
]