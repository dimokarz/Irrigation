# from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import VideoSrv, Cameras
from .serializers import VideoSrvSerializer, CamerasSerializer


### Видеосерверы
@api_view(['GET'])
def videosrv_list(request):
    videoSrv = VideoSrv.objects.all()
    serializer = VideoSrvSerializer(videoSrv, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def videosrv_detail(request, pk):
    try:
        videoSrv = VideoSrv.objects.get(id=pk)
        serializer = VideoSrvSerializer(videoSrv)
    except VideoSrv.DoesNotExist as err:
        return Response(status.HTTP_404_NOT_FOUND)
    return Response(serializer.data, status.HTTP_200_OK)


@api_view(['POST'])
def videosrv_create(request):
    serializer = VideoSrvSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status.HTTP_201_CREATED)


@api_view(['PUT'])
def videosrv_update(request, pk):
    try:
        videoSrv = VideoSrv.objects.get(id=pk)
        serializer = VideoSrvSerializer(videoSrv, data=request.data)
        if serializer.is_valid():
            serializer.save()
    except VideoSrv.DoesNotExist as err:
        return Response(status.HTTP_404_NOT_FOUND)
    return Response(serializer.data, status.HTTP_200_OK)


@api_view(['DELETE'])
def videosrv_delete(request, pk):
    videoSrv = VideoSrv.objects.get(id=pk)
    videoSrv.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


### Камеры
@api_view(['GET'])
def cameras_list(request):
    cameras = Cameras.objects.all()
    serializer = CamerasSerializer(cameras, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def cameras_detail(request, pk):
    try:
        cameras = Cameras.objects.get(id=pk)
        serializer = CamerasSerializer(cameras)
    except Cameras.DoesNotExist as err:
        return Response(status.HTTP_404_NOT_FOUND)
    return Response(serializer.data, status.HTTP_200_OK)


@api_view(['POST'])
def cameras_create(request):
    serializer = CamerasSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status.HTTP_201_CREATED)