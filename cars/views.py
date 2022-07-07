from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import cars

# Create your views here.

@api_view(["POST", "GET"])
def getCars(request, *args, **kwargs):
    
    if request.method == "POST":
        
        fabricante = request.data.get("fabricante")
        marca = request.data.get("marca")
        cilindraje = request.data.get("cilindraje")

        car = cars(fabricante=fabricante, marca=marca, cilindraje=cilindraje)
        car.save()

        return Response({
            "data" : {
                "fabricante" : car.fabricante,
                "marca" : car.marca,
                "cilindraje" : car.cilindraje
            }
        })

    if request.method == "GET":

        _cars = cars.objects.all()

        return Response({
            "data" : [{
                "fabricante" : car.fabricante,
                "marca" : car.marca,
                "cilindraje" : car.cilindraje
            } for car in _cars]
        })