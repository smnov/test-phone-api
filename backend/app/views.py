from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
import time
import random
import string


class InvitedUsersView(APIView):
    def post(self, request):
        user = request.user
        invited_users = User.objects.filter(invite_code=user.invite_code).exclude(id=user.id)
        invited_user_phone_numbers = [u.phone_number for u in invited_users]
        return Response(invited_user_phone_numbers, status=status.HTTP_200_OK)


class UserProfileView(APIView):
    def get(self, request):
        phone_number = request.data.get('phone_number')
        try:
            user = User.objects.filter(phone_number=phone_number)
            serializer = UserSerializer(user, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class SendAuthCode(APIView):

    def generate_invite_code(self):
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        return code
    
    def generate_auth_code(self):
        code = str(random.randint(1000, 9999))
        return code
    
    def post(self, request):
        phone_number = request.data.get('phone_number')
        auth_code = self.generate_auth_code()
        invite_code = self.generate_invite_code()
        time.sleep(2) 
        user = User(phone_number=phone_number, auth_code=auth_code, invite_code=invite_code)
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CheckAuthCode(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        auth_code = request.data.get('auth_code')
        try:
            user = User.objects.get(phone_number=phone_number, auth_code=auth_code)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)