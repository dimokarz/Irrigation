from rest_framework import serializers
from .models import VideoSrv, Cameras


class VideoSrvSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoSrv
        fields = '__all__'


class CamerasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cameras
        fields = '__all__'