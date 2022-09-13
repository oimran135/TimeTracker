from rest_framework import serializers

from .models import (
    UserDailyLogs,
    UserProjectDailyLogs,
)


class UserLogsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserDailyLogs
        fields = '__all__'


class UserProjectLogsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProjectDailyLogs
        fields = '__all__'
