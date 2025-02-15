from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Issue, Comment
from .serializers import IssueSerializer, CommentSerializer

# Create your views here.




@api_view(['GET'])
def hello(request):
    return Response({
        'success': True,
        'message': 'Working!',
        'data': {}
    }, status=status.HTTP_200_OK)

class IssueAPIView(APIView):
    def get(self, request, pk=None):
        if pk == None:
            try:
                issue = Issue.objects.get(pk=pk)
                seralizer = IssueSerializer(issue)
                return Response(seralizer.data)
            except:
                return Response({}, status=status.HTTP_404_NOT_FOUND)
        else:
            issues = Issue.objects.all()
            seralizer = IssueSerializer(issues, many=True)
            return Response(seralizer.data)


    def post(self, request):
        serializer = IssueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

    # def put(self, request):
    #     pass

    # def delete(self, request):
    #     pass