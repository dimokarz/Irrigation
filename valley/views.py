from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Systems, States
from .serializers import SystemsSerializer, StatesSerializer


### Системы полива
@api_view(['GET'])
def systems_list(request):
    systems = Systems.objects.all()
    serializer = SystemsSerializer(systems, many=True)
    return Response(serializer.data)


### Состояния систем
@api_view(['GET'])
def states_list(request):
    states = States.objects.all()
    serializer = StatesSerializer(states, many=True)
    return Response(serializer.data)


### index
def index(request):
    systems = Systems.objects.all()
    states = States.objects.all()
    header = 'Выбор систем полива'
    title = ' - Выбор'
    return render(request, 'index.html', {'header': header, 'title': title, 'systems': systems, 'states': states})
