from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer,UserChangePasswordSerializer
from django.contrib.auth import authenticate
from .renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

# Create your views here.


def get_tokens_for_user(user):
    print("get Token",user)
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]
    def post(self,request,format=None):
        serializer = UserRegistrationSerializer(data=request.data)

        # if we want to check that there's "ErrorDetails" key in every error we need to remove the argument of raise_exception 
        # from the is_valid() parenthesis
        if serializer.is_valid():
            user=serializer.save()
            token = get_tokens_for_user(user)
            return Response({'token':token,'msg':"Registration Successful"},status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    



class UserLoginView(APIView):
    renderer_classes = [UserRenderer]

    def post(self,request,format=None):
        serializer = UserLoginSerializer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            print(user)
            if user is not None: 
                token = get_tokens_for_user(user)

                return Response({"token":token,'msg':'Login Success'}, status = status.HTTP_200_OK)
            else: 
                return Response({'errors': {'non_field_erros': ['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializer.erros,status = status.HTTP_400_BAD_REQUEST)
    


class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        print(request.user)
        serializer = UserProfileSerializer(request.user)
        # if serializer.is_valid():
        return Response(serializer.data,status = status.HTTP_200_OK)
    

class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        serializer = UserChangePasswordSerializer(data = request.data, context = {'user':request.user})
        if serializer.is_valid(raise_exception = True):
            return Response({'msg':'Password Changed Successfully'},status = status.HTTP_200_OK)
        return Response(serializer.erros,status = status.HTTP_400_BAD_REQUEST)
        
    