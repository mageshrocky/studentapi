from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from .models import StudentDetails, Subject
from .serializers import StudentValidation, SubjectValidation
from rest_framework.response import Response


# Create your views here.


@api_view(['POST', 'GET'])
def create_student(request):
    if request.method == 'POST':
        serializer_data = StudentValidation(data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data)
        return Response(serializer_data.data)

    if request.method == 'GET':
        record = StudentDetails.objects.all()
        result = StudentValidation(record, many=True)
        return Response(result.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT'])
def update_student_details(request, rn):
    try:
        record = StudentDetails.objects.get(Roll_Number=rn)
    except Exception as e:
        print(e)
    if request.method == 'GET':
        record = StudentDetails.objects.filter(Roll_Number=rn)
        result = StudentValidation(record, many=True)
        return Response(result.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        result = StudentValidation(record, data=request.data)
        if result.is_valid():
            result.save()
            return Response(result.data, status=status.HTTP_201_CREATED)
        return Response('Bad request', status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def add_mark(request):
    if request.method == 'GET':
        record = Subject.objects.all()
        result = SubjectValidation(record, many=True)
        return Response(result.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        result = SubjectValidation(data=request.data)
        if result.is_valid():
            result.save()
            return Response(result.data, status=status.HTTP_201_CREATED)
        return Response(result.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def update_mark(request, id):
    if request.method == 'GET':
        record = Subject.objects.filter(id=id)
        result = SubjectValidation(record, many=True)
        return Response(result.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        record = Subject.objects.get(id=id)
        result = SubjectValidation(record, data=request.data)
        if result.is_valid():
            result.save()
            return Response(result.data, status=status.HTTP_200_OK)
        return Response(result.data, status=status.HTTP_400_BAD_REQUEST)

