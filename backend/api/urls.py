from django.urls import path, include

from api.views import GoogleLogin, GoogleRedirect, UserData

urlpatterns = [
    path('auth/google/login/', GoogleRedirect.as_view(), name='google_login_redirect'),
    path('auth/google/login/success', GoogleLogin.as_view(), name='google_login_fetch_data'),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),

    path('user/', UserData.as_view(), name='user_data'),
]
