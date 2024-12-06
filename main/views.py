from django.shortcuts import render

# Create your views here.
from .models import Brand, Car

def home(request):
    brands = Brand.objects.all()  # Fetch all brand data
    cars = Car.objects.all()  # Fetch all car data
    return render(request, 'home.html', {'brands': brands, 'cars': cars})
