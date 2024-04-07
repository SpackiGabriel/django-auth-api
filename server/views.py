from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes
)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication
)
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer


@api_view(['POST'])
def login(request: Request) -> Response:
    """
    Logs in a user and returns a token and user information.

    Args:
        request (Request): The HTTP request object.

    Returns:
        Response: The HTTP response object containing the token and user information.

    Raises:
        Http404: If the user with the specified username is not found.
    """
    user = get_object_or_404(User, username=request.data['username'])

    if not user.check_password(request.data['password']):
        return Response(
            {
                'error': 'Invalid password'
            },
            status=status.HTTP_401_UNAUTHORIZED
        )

    token, _ = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)

    return Response(
        {
            'token': token.key,
            'user': serializer.data
        }
    )

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
    serializer = UserSerializer(data = request.data)
    
    if serializer.is_valid():
        user = serializer.save()

        user.set_password(request.data['password'])
        user.save()

        token = Token.objects.create(user = user)
        
        return Response(
            {
                'token': token.key,
                'user': serializer.data
            }
        )

    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def verify(request: Request) -> Response:
    """
    View function to verify if a user is authenticated.

    Args:
        request (Request): The HTTP request object.

    Returns:
        Response: The HTTP response object containing a message and user data.
    """
    return Response(
        {
            'message': 'User is authenticated',
            'user': UserSerializer(instance=request.user).data
        }
    )
