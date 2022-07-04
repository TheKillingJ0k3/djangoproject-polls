# Python

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
] # next step: point the root URLconf at the polls.urls module