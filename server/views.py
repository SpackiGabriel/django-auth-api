from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .serializers import UserSerializer


@api_view(['POST'])
def login(request: Request) -> Response:
    return Response({})

@api_view(['POST'])
def register(request: Request) -> Response:
    """
    Register a new user.

    Args:
        request (Request): The HTTP request object.

    Returns:
        Response: The HTTP response object containing the token and user data if successful,
        or the error message and status code if unsuccessful.
    """
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        user = serializer.save()

        user.set_password(request.data['password'])
        user.save()

        token = Token.objects.create(user=user)
        
        return Response(
            {
                'token': token.key,
                'user': serializer.data
            }
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def verify(request: Request) -> Response:
    return Response({})