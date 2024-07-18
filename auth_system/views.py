from django.contrib.auth.models import User
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from random import randint
from django.conf import settings
from django.utils import timezone
import datetime
from rest_framework_simplejwt.tokens import RefreshToken

OTP_STORE = {}

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            if User.objects.filter(email=email).exists():
                return Response({"message": "Email already exists."}, status=status.HTTP_400_BAD_REQUEST)
            User.objects.create_user(username=email, email=email)
            return Response({"message": "Registration successful. Please verify your email."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RequestOTPView(APIView):
    def post(self, request):
        email = request.data.get('email')
        if not User.objects.filter(email=email).exists():
            return Response({"message": "Email not registered."}, status=status.HTTP_400_BAD_REQUEST)
        otp = randint(100000, 999999)
        OTP_STORE[email] = {'otp': otp, 'timestamp': timezone.now()}
        send_mail(
            'Your OTP Code',
            f'Your OTP code is {otp}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        return Response({"message": "OTP sent to your email."})



class VerifyOTPView(APIView):
    def post(self, request):
        email = request.data.get('email')
        otp = request.data.get('otp')
        if email in OTP_STORE and OTP_STORE[email]['otp'] == int(otp):
            timestamp = OTP_STORE[email]['timestamp']
            if timezone.now() - timestamp > datetime.timedelta(minutes=1):
                return Response({"message": "OTP expired."}, status=status.HTTP_400_BAD_REQUEST)
            del OTP_STORE[email]

            user = User.objects.get(email=email)
            refresh = RefreshToken.for_user(user)
            return Response({
                "message": "Login successful.",
                "token": str(refresh.access_token),
                "refresh": str(refresh)
            })
        return Response({"message": "Invalid OTP."}, status=status.HTTP_400_BAD_REQUEST)
