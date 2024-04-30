from crud import serializer
from crud.models import DetailsModel
from .serializer import DetailsSerializer
from crud.models import CreateTaxModel
from .serializer import CreateTaxModelSerializer
from .serializer import UserSignupSerializer
from .serializer import UserLoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse


#signup
class UserSignup(APIView):
    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                try:
                    # Generate token for the user
                    token, _ = Token.objects.get_or_create(user=user)
                    return Response({'token': token.key})
                except Exception as e:
                    return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response({'error': 'User creation failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#login
class UserLogin(APIView):
    authentication_classes = [] 
    permission_classes = []  

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                token, _ = Token.objects.get_or_create(user=user)
                return JsonResponse({'token': token.key})
            else:
                return JsonResponse({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 
class UserAuthView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            return JsonResponse({'ok': True})
        else:
            return JsonResponse({'ok': False})
    
