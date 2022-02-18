from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Events
from .serializers import EventSerializer
from django.conf import settings
from django.http.response import Http404
from django.db.models import Max

User = settings.AUTH_USER_MODEL

# @api_view(['GET'])
# @permission_classes([AllowAny])
# def get_video_comments(request, video_id):
#     comment = Comment.objects.filter(video_id=video_id)  
#     serializer = CommentSerializer(comment,many=True)
#     return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def add_entry(request):
    if request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_entries(request, fk):
    records = Events.objects.filter(user_id=fk).order_by('date')  
    serializer = EventSerializer(records, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_entry(request, pk):
    try:
        comment = Events.objects.get(id=pk)
        serializer  = EventSerializer(comment)
        comment.delete()
        return Response(serializer.data)
    except Events.DoesNotExist:
        raise Http404
