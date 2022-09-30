from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *

# @api_view(['GET'])
# def apiOverview(request):
#     api_urls = {
#         'List':'/studentlist/',
#         'Detail view':'/studentdetail/<str:pk>/',
#         'create':'/studentcreate/',
#         'update':'/studentupdate/<str:pk/',
#         'delete':'/studentdelete/<str:pk>/'
#     }
#     return Response('api_urls')

@api_view(['GET'])
def StudentList(request):
    data = Student.objects.all()
    serializer = StudentSerializer(data,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def StudentDetail(request,pk):
    data = Student.objects.get(id=pk)
    serializer = StudentSerializer(data,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def StudentCreate(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def StudentUpdate(request,pk):
    data = Student.objects.get(id=pk)
    serializer = StudentSerializer(instance=data,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def StudentDelete(request,pk):
    data = Student.objects.get(id=pk)
    data.delete()
    return Response("Item deleted")

