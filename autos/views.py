from django.shortcuts import render
from .models import Auto

# Create your views here.
def Autos(request):
    
    autos = Auto.objects.all()
    return (render(request, "autos.html", {'autos':autos}))