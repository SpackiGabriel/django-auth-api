from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .serializers import UserSerializer


@api_view(['POST'])
def login(request: Request) -> Response:
    return Response

@api_view(['POST'])
def register(request: Request) -> Response:
    return Response


@api_view(['POST'])
def verify(request: Request) -> Response:
    return Response