from rest_framework import serializers

from .models import (
    Project,
    UserRole,
    UserProjectRole,
)

class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = '__all__'


class UserRoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserRole
        fields = '__all__'


class UserProjectRoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProjectRole
        fields = '__all__'