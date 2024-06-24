from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path('logeo/',views.logeo, name='logeo'),
]