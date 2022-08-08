# from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Systems, States
from .serializers import SystemsSerializer, StatesSerializer


@api_view(['GET'])
def systems_list(request):
    Systems.objects.all()
    serializer = SystemsSerializer
    return Response(serializer.data)


@api_view(['GET'])
def states_list(request):
    states = States.objects.all()
    serializer = StatesSerializer
    return Response(serializer.data)
