from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from django.shortcuts import redirect
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

class GoogleRedirect(APIView):
    def get(self, request, *args, **kwargs):
        google_login_url = reverse('google_login')
        return Response({"redirect_url": f"http://localhost:8000{google_login_url}"}, status=200)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'profile_picture']

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter

    def get(self, request, *args, **kwargs):
        user = request.user

        if not user.is_authenticated:
            return Response({"error": "User not authenticated"}, status=401)
        
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)


        redirect_url = 'http://localhost:5173/auth/success'
        params = f'?access_token={access_token}&refresh_token={refresh}'
        print(f'{redirect_url}{params}')
        return redirect(f'{redirect_url}{params}')
    
class UserData(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        data = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "profile_picture": getattr(user, 'profile_picture', None)
        }
        return Response(data)
