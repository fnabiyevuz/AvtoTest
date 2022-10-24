from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('bilet/<int:id>/<int:num>', bilet),
]