from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import ExerciseActivity
from .serializers import ExerciseActivitySerializer
from django.conf import settings
from django.http.response import Http404

User = settings.AUTH_USER_MODEL

# @api_view(['GET'])
# @permission_classes([AllowAny])
# def get_video_comments(request, video_id):
#     comment = Comment.objects.filter(video_id=video_id)  
#     serializer = CommentSerializer(comment,many=True)
#     return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def add_weight(request):
    if request.method == 'POST':
        serializer = ExerciseActivitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_weight(request, fk):
    records = ExerciseActivity.objects.filter(user_id=fk)  
    serializer = ExerciseActivitySerializer(records, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_weight(request, pk):
    try:
        comment = ExerciseActivity.objects.get(id=pk)
        serializer  = ExerciseActivitySerializer(comment)
        comment.delete()
        return Response(serializer.data)
    except ExerciseActivity.DoesNotExist:
        raise Http404

@api_view(['GET'])
@permission_classes([AllowAny])
def get_one_weight(request, pk):
    try:
        comment = ExerciseActivity.objects.get(id=pk)
        serializer  = ExerciseActivitySerializer(comment)
        return Response(serializer.data)
    except ExerciseActivity.DoesNotExist:
        raise Http404

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_weight(request, pk):
    record = ExerciseActivity.objects.get(id=pk)
    serializer = ExerciseActivitySerializer(record, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)