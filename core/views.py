from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import UserDetails
from .serializers import UserDetailsSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK

from django.http import Http404

from django.contrib.auth.hashers import make_password, check_password

@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        user = UserDetails.objects.all()
        serializer = UserDetailsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
    
    return render(request, 'registration.html')


class LoginView(APIView):

    def post(self,request):
        user  = request.data
        print(user)
        serializer = LoginSerializer(data = user)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            return Response({
                "message":"Login Successfull",
                "user":{
                    "id": user.id,
                    "name":user.name,
                    "email":user.email,
                }
            }, status = HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
# class LoginView(APIView):
#     def post(self, request):
#         data = request.data  
#         # user_id = data.get("id")
#         print(user_id)

#         password = data.get("password")

#         if not user_id or not password:
#             return Response({"error": "Both ID and password are required"}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             user = UserDetails.objects.get(id=user_id)
#             if user.password != password:
#                 return Response({"error": "Incorrect password"}, status=status.HTTP_401_UNAUTHORIZED)

#             return Response({"message": "Login successful"}, status=status.HTTP_200_OK)

#         except UserDetails.DoesNotExist:
#             return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
