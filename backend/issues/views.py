from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.




@api_view(['GET'])
def hello(request):
    return Response({
        'success': True,
        'message': 'Working!',
        'data': {}
    }, status=status.HTTP_200_OK)