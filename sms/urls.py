from django.urls import path

from . import views

urlpatterns = [
    path('', views.sms_form, name='form'),
    path('send/', views.send_sms, name='send')
]