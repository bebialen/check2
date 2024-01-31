from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from django.shortcuts import get_object_or_404


@api_view(['POST'])
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def get_all_students(request):
    students = Student.objects.all().order_by('name')
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_single_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    serializer = StudentSerializer(student)
    return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
def update_delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=204)
    else:
        return Response({'message': 'Method not allowed'}, status=405)