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

class IssueListCreateAPIView(APIView):
    def get(self, request):
        issues = Issue.objects.all()
        seralizer = IssueSerializer(issues, many=True)
        return Response({"success": True, "data": seralizer.data})


    def post(self, request):
        serializer = IssueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success":True, "data":serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
class IssueDetailUpdateDeleteAPIView(APIView):
    
    def get(self, request, pk):
        try:
            issue = Issue.objects.get(pk=pk)
            seralizer = IssueSerializer(issue)
            return Response({"success": True, "data":seralizer.data})
        except:
            return Response({"success": False, "errors": "Issue with given ID not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            issue = Issue.objects.get(pk=pk)
            seralizer = IssueSerializer(issue, data=request.data, partial=True)
            if seralizer.is_valid():
                seralizer.save()
                return Response({"success": True, "data":seralizer.data})
            return Response({"success": False, "errors": seralizer.errors}, status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response({"success": False, "errors": "Issue with given ID not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            issue = Issue.objects.get(pk=pk)
            issue.delete()
            return Response({"success": True, "message": "Deleted the issue successfully!"}, status=status.HTTP_200_OK)
        
        except:
            return Response({"success": False, "errors": "Issue with given ID not found"}, status=status.HTTP_404_NOT_FOUND)

class CommentListCreateAPIView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        issue_id = request.data.get('issue')
        if not issue_id:
            return Response({"success": False, "errors": "Issue ID is missing"}, status=status.HTTP_400_BAD_REQUEST)

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
    
class CommmentDetailUpdateDeleteAPIView(APIView):

    def get(self, request, pk):
        try:
            comment = Comment.objects.get(pk=pk)
            serializer = CommentSerializer(comment)
            return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"success": False, "errors": "Comment with given ID not found"}, status=status.HTTP_404_NOT_FOUND)

        
    def put(self, request, pk):
        try:
            comment = Comment.objects.get(pk=pk)
            seralizer = CommentSerializer(comment, data=request.data, partial=True)
            print("pre comment serial validation")
            if seralizer.is_valid():
                print("comment serial validation")
                seralizer.save()
                return Response({"success": True, "data":seralizer.data})
            return Response({"success": False, "errors": seralizer.errors}, status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response({"success": False, "errors": "Comment with given ID not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            comment = Comment.objects.get(pk=pk)
            comment.delete()
            return Response({"success": True, "message": "Deleted the comment successfully!"}, status=status.HTTP_200_OK)
        
        except:
            return Response({"success": False, "errors": "Comment with given ID not found"}, status=status.HTTP_404_NOT_FOUND)

        
        