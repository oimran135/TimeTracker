from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from .models import (
    Project,
    UserRole,
    UserProjectRole,
)

from .serializers import (
    ProjectSerializer,
    UserRoleSerializer,
    UserProjectRoleSerializer,
)


class ProjectView(APIView):

    permission_classes = (permissions.IsAdminUser,)

    def get_queryset(self, request, pk=None):
        try:
            queryset = Project.objects.get(pk=pk)
            return queryset
        except Project.DoesNotExist:
            return Response({'message':'No project exists with this ID.'})

    def get(self, request):
        queryset = self.get_queryset(request)
        serializer = ProjectSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProjectSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, pk=None):
        queryset = Project.objects.get(pk=pk)
        serializer = ProjectSerializer(queryset, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)        


class UserRoleView(APIView):
    
    def post(self, request):
        serializer = UserRoleSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserProjectRoleView(APIView):
    
    def post(self, request):
        serializer = UserProjectRoleSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
