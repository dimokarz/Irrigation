from django.shortcuts import render
from rest_framework import status
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Systems, States, KeyBoard
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
    header = 'Выбор систем полива'
    title = ' - Выбор'
    return render(request, 'index.html', {'header': header, 'title': title, 'systems': systems})


## simple
def simple(request):
    first = request.GET.get('first')
    second = request.GET.get('second')
    valList = [first]
    if second != '0':
        valList.append(second)
    systems = Systems.objects.all().in_bulk(valList).values()
    states = States.objects.all().in_bulk(valList).values()
    keyboard = KeyBoard.objects.filter(id__range=[25, 32])
    return render(request, 'simple.html', {'systems': systems, 'states': states, 'keyboard': keyboard})
