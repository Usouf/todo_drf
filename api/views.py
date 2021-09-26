from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action

from .serializers import TaskSerializer

from .models import *

# Create your views here.
class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializer

    @action(detail = True, methods = ['get'])
    def get_recent_by_name(self, request, name = None):
        tasks = self.objects.filter(name__icontains = name)
        serializer = TaskSerializer(tasks, many = True)
        return Response(serializer.data)

# class TaskView(APIView):
#     def get(self, format=None):
#         tasks = Task.objects.all()
#         serializer = TaskSerializer(tasks, many = True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = TaskSerializer(data = request.data)
#         if serializer.is_valid(raise_exception=ValueError):
#             serializer.create(validated_data=request.data)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.error_messages,
#                         status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request):
#

# @api_view(['GET'])
# def apiOverview(request):
#     api_urls = {
# 		'List':'/task-list/',
# 		'Detail View':'/task-detail/<str:pk>/',
# 		'Create':'/task-create/',
# 		'Update':'/task-update/<str:pk>/',
# 		'Delete':'/task-delete/<str:pk>/',
# 		}
#     return Response(api_urls)
#
# @api_view(['GET'])
# def taskList(request):
#     tasks = Task.objects.all()
#     serializer = TaskSerializer(tasks, many=True)
#     return Response(serializer.data)
#
# @api_view(['GET'])
# def taskDetail(request, pk):
#     task = Task.objects.get(id=pk)
#     serializer = TaskSerializer(task, many=False)
#     return Response(serializer.data)
#
# @api_view(['POST'])
# def taskCreate(request):
# 	serializer = TaskSerializer(data=request.data)
#
# 	if serializer.is_valid():
# 		serializer.save()
#
# 	return Response(serializer.data)
#
# @api_view(['POST'])
# def taskUpdate(request, pk):
# 	task = Task.objects.get(id=pk)
# 	serializer = TaskSerializer(instance=task, data=request.data)
#
# 	if serializer.is_valid():
# 		serializer.save()
#
# 	return Response(serializer.data)
#
# @api_view(['DELETE'])
# def taskDelete(request, pk):
# 	task = Task.objects.get(id=pk)
# 	task.delete()
#
# 	return Response('Item succsesfully delete!')
