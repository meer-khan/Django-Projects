from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.views import APIView
from .serializers import (UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer,
                          UserChangePasswordSerializer,SendPasswordResetEmailSerializer,UserPasswordResetSerializer)
from django.contrib.auth import authenticate
from .renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .models import BlackListedTokens

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
        print(request.data)
        serializer = UserRegistrationSerializer(data=request.data)
        print("Serializer : ", serializer)
        # if we want to check that there's "ErrorDetails" key in every error we need to remove the argument of raise_exception 
        # from the is_valid() parenthesis
        if serializer.is_valid():
            user=serializer.save()
            token = get_tokens_for_user(user)
            return Response({'token':token,'msg':"Registration Successful"},status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        # serializer.is_valid(raise_exception=True)
        # user = serializer.save()
        # token = get_tokens_for_user(user)
        # return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)





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
                return Response({'errors': {'non_field_errors': ['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializer.erros,status = status.HTTP_400_BAD_REQUEST)
    


class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        
        serializer = UserProfileSerializer(request.user)
        # if serializer.is_valid():

        # CHECKING BLACKLISTED TOKEN
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if auth_header.startswith('Bearer '):
            token = auth_header[len('Bearer '):]
            print("Token in Profile :", token)
            print(BlackListedTokens.objects.filter(token=token).exists())
        if BlackListedTokens.objects.filter(token=token).exists():
            return Response({'error':"Token has expired"},status = status.HTTP_400_BAD_REQUEST)



        print("In Profile View: ",request.user)
        return Response(serializer.data,status = status.HTTP_200_OK)
    

class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def put(self,request,format=None):
        print(request.data)
        serializer = UserChangePasswordSerializer(data = request.data, context = {'user':request.user})
        if serializer.is_valid(raise_exception = True):


            # *Blacklisting the token

            auth_header = request.META.get('HTTP_AUTHORIZATION', '')
            if auth_header.startswith('Bearer '):
                token = auth_header[len('Bearer '):]
            # Now you have the token and can use it as needed
            # For example, you can pass it to your custom authentication class
            # for token verification or blacklisting
            # Do whatever you need to do with the token
                print("Token:", token)

            blacklisted_token = BlackListedTokens(token=token)
            blacklisted_token.save()




            return Response({'msg':'Password Changed Successfully'},status = status.HTTP_200_OK)
        return Response(serializer.erros,status = status.HTTP_400_BAD_REQUEST)
        

class SendPasswordResetEmailView(APIView):
    renderer_classes = [UserRenderer]
    def post(self,request,format=None):
        serializer = SendPasswordResetEmailSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):

            return Response({'msg':'Password Reset link send. Please check your Email'}, status = status.HTTP_200_OK) 
        return Response(serializer.erros,status = status.HTTP_400_BAD_REQUEST)
    


class UserPasswordResetView(APIView): 
    renderer_classes = [UserRenderer]
    def post(self,request,uid,token, format=None): 
        serializer = UserPasswordResetSerializer(data=request.data,context = {'uid':uid,'token':token})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password Reset Successfully'}, status = status.HTTP_200_OK)
        return Response(serializer.erros,status = status.HTTP_400_BAD_REQUEST)
    






class FileUploadRequest(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        serializer = UserProfileSerializer(request.user)
        if serializer.is_valid(raise_exception=True):
            print("In Profile View: ",request.user)
            return Response(serializer.data,status = status.HTTP_200_OK)
        

class UserBOMResults(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        serializer = UserProfileSerializer(request.user)
        if serializer.is_valid(raise_exception=True):
            print("In Profile View: ",request.user)
            return Response(serializer.data,status = status.HTTP_200_OK)

    
    