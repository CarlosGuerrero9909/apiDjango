from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import users

# Create your views here.

@api_view(["POST", "GET"])
def getUsers(request, *args, **kwargs):

    if request.method == 'POST':
        username = request.data.get("username")
        number = request.data.get("number")

        user = users(username=username, number=number)
        user.save()

        return Response({
            "data" : {
                "username" : user.username,
                "number" : user.number,
            }
        })

    if request.method == 'GET':
        _users = users.objects.all()

        return Response({
            "data" : [{
                "username" : user.username,
                "number" : user.number,
            } for user in _users]
        })
