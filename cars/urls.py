from django.contrib import admin
from django.urls import path, include #include asocia un concepto general a urls especificas
from .views import *

urlpatterns = [
    path('getALL/', getCars),

]