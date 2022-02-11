from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Exercise
from .serializers import ExerciseSerializer
from django.contrib.auth.models import User
from django.http.response import Http404

@api_view(['POST'])
@permission_classes([AllowAny])
def add_exercises(request):
    if request.method == 'POST':
        serializer = ExerciseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_exercises(request, pk):
    try:
        comment = Exercise.objects.get(id=pk)
        serializer  = ExerciseSerializer(comment)
        comment.delete()
        return Response(serializer.data)
    except Exercise.DoesNotExist:
        raise Http404

@api_view(['GET'])
@permission_classes([AllowAny])
def get_exercise(request, pk):
    try:
        comment = Exercise.objects.get(id=pk)
        serializer  = ExerciseSerializer(comment)
        return Response(serializer.data)
    except Exercise.DoesNotExist:
        raise Http404

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_exercises(request):
    comment = Exercise.objects.all()  
    serializer = ExerciseSerializer(comment,many=True)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_exercise(request, pk):
    comment = Exercise.objects.get(id=pk)
    serializer = ExerciseSerializer(comment, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)