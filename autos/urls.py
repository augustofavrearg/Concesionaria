
from django.urls import path
from django.urls import URLPattern
from .views import Autos

app_name = 'autos'

urlpatterns=[
    path('autos/', Autos, name="autos")
]