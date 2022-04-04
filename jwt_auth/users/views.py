from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JSONWebTokenAuthentication])
def test(request):
    return HttpResponse('success')
