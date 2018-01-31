from django.urls import path

from . import views

app_name = 'message'

urlpatterns = [
    path('message',views.send_message,name='send_message')
]
