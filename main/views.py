from django.shortcuts import render

# Create your views here.
from .models import Brand, Car

def home(request):
    brands = Brand.objects.all()
    cars = Car.objects.all()
    return render(request, 'home.html', {'brands': brands, 'cars': cars})

def brand_cars(request, brand_id):
    try:
        brand = Brand.objects.get(id=brand_id)
        cars = brand.cars.all()
    except Brand.DoesNotExist:
        brand = None
        cars = []
    return render(request, 'brand.html', {'brand': brand, 'cars': cars})

def car_detail(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        car = None
    return render(request, 'car.html', {'car': car})

