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
        if pk:
            try:
                issue = Issue.objects.get(pk=pk)
                seralizer = IssueSerializer(issue)
                return Response({"success": True, "data":seralizer.data})
            except:
                return Response({}, status=status.HTTP_404_NOT_FOUND)
        else:
            issues = Issue.objects.all()
            seralizer = IssueSerializer(issues, many=True)
            return Response({"success": True, "data": seralizer.data})


    def post(self, request):
        serializer = IssueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success":True, "data":serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

    # def put(self, request):
    #     pass

    # def delete(self, request):
    #     pass

class CommentAPIView(APIView):
    def get(self, request, pk=None):
        try:
            if pk:
                comment = Comment.objects.get(pk=pk)
                serializer = CommentSerializer(comment)
                return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)
            comments = Comment.objects.all()
            serializer = CommentSerializer(comments, many=True)
            return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"success": False, "message": "Something went wrong", "errors": {str(e)}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self, request):
        issue_id = request.data.get('issue')

        try:
            issue = Issue.objects.get(pk=issue_id)
        except Exception as e:
            return Response({"success": False, "message": f"issue with given ID ({issue_id}) doesn't exist", "errors": {str(e)}}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            # Serializers won't automatically save the related fields unless they are explicitly passed to the serializer.
            serializer.save(issue=issue)
            return Response({"success": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
    
        return Response({"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        