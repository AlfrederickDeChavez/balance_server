from django.contrib.auth import get_user_model
from rest_framework import status

from accounts.serializer import UserSerializer, UpdateUserSerializer
User = get_user_model()
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import permissions


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny, ]
    
    def post(self, request, format=None):
        data = self.request.data
        username = data['username']
        email = data['email']
        password = data['password']
        password2 = data['password2']
        age = data['age']
        gender = data['gender']
        height = data['height']
        weight = data['weight']

        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({'response': 'error', 'message': 'Email already exist.'})
            else:
                if len(password) < 6:
                    return Response({'response': 'error', 'message': 'Password must be at least 6 characters.'})
                else: 
                    user = User.objects.create_user(email=email, username=username, password=password, age=age, gender=gender, height=height, weight=weight)
                    user.save()
                    return Response({'response': 'success', 'message': 'User created successfully.'})
        else:
            return Response({'response': 'error', 'message': 'Password does not match.'})

class UserDetailsView(APIView): 
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK) 

class UpdateProfileView(APIView):

    permission_classes = [permissions.IsAuthenticated,  ]

    def put(self, request):
        user = request.user
        serializer = UpdateUserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
        
    

