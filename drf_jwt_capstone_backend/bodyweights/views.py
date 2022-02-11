from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import BodyWeight
from .serializers import BodyWeightSerializer
from django.conf import settings
from django.http.response import Http404

User = settings.AUTH_USER_MODEL

@api_view(['POST'])
@permission_classes([AllowAny])
def add_bodyweight(request):
    if request.method == 'POST':
        serializer = BodyWeightSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_bodyweight(request, fk):
    records = BodyWeight.objects.filter(user_id=fk)  
    serializer = BodyWeightSerializer(records, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_bodyweight(request, pk):
    try:
        comment = BodyWeight.objects.get(id=pk)
        serializer  = BodyWeightSerializer(comment)
        comment.delete()
        return Response(serializer.data)
    except BodyWeight.DoesNotExist:
        raise Http404

@api_view(['GET'])
@permission_classes([AllowAny])
def get_one_bodyweight(request, pk):
    try:
        comment = BodyWeight.objects.get(id=pk)
        serializer  = BodyWeightSerializer(comment)
        return Response(serializer.data)
    except BodyWeight.DoesNotExist:
        raise Http404

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_bodyweight(request, pk):
    record = BodyWeight.objects.get(id=pk)
    serializer = BodyWeightSerializer(record, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)