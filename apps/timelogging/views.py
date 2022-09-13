from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from datetime import datetime

from apps.project.models import UserProjectRole

from .models import (
    UserDailyLogs,
    UserProjectDailyLogs,
)

from .serializers import (
    UserLogsSerializer,
    UserProjectLogsSerializer,
)


class UserDailyCheckInView(APIView):
    '''
        This API will be hit everyday when the user checks in to their work poral.
        This can also be considered a mark of presence.
    '''
    
    def post(self, request):
        now = datetime.now().time()
        user_id = request.user.id
        request.data['user'] = user_id
        request.data['start_time'] = now
        serializer = UserLogsSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserDailyCheckOutView(APIView):
    '''
        This API will be hit at the end of the day when user is done with their work.
        To demonstrate businesslogic, let's assume the request is empty.
    '''
    def patch(self, request, pk=None):
        queryset = UserDailyLogs(pk=pk)
        now = datetime.now().time()
        request.data['end_time'] = now
        serializer = UserLogsSerializer(queryset, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)     


class UserProjectCheckInView(APIView):
    '''
        This API will be hit everytime the user checks-in to work on a project.
    '''
    def post(self, request):
        now = datetime.now().time()
        request.data['start_time'] = now

        date = datetime.date.today()
        request.data['date'] = date

        user_id = request.user.id

        # Will be sent with the request to get the right object
        project = request.data['project']
        role = request.data['role']
        del request.data['project']
        del request.data['role']
        user_project_role = UserProjectRole.objects.filter(user=user_id, project=project, role=role)[0]
        request.data['user_project_role'] = user_project_role.id

        serializer = UserProjectLogsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserProjectCheckOutView(APIView):
    '''
        This API will be hit everytime the user is done working on a project
        for the day or iteration. These logs can be kept for future reference
        to determine how much the user has worked on a project in a particular
        role.
    '''
    def patch(self, request):
        date = datetime.date.today()

        user_id = request.user.id

        # Will be sent with the request to get the right object
        project = request.data['project']
        role = request.data['role']
        del request.data['project']
        del request.data['role']
        user_project_role = UserProjectRole.objects.filter(user=user_id, project=project, role=role)[0]
        user_project_role_id = user_project_role.id

        request.data['end_time'] = datetime.now().time()

        queryset = UserProjectDailyLogs.objects.filter(user_project_role=user_project_role_id, date=date)[0]
        serializer = UserProjectLogsSerializer(queryset, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
