from rest_framework import serializers
from .models import Systems, States


class SystemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Systems
        fields = '__all__'


class StatesSerializer(serializers.ModelSerializer):
    system_name = serializers.StringRelatedField()

    class Meta:
        model = States
        fields = '__all__'
