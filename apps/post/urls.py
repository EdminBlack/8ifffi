from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('contact/', contact),
    path('time/', time),
    path('aboat/', aboat),
    path('weather/', weather)
]