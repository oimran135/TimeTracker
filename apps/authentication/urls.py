from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import (
    RegisterView,
    LogoutView,
    UserView,
    UpdatePasswordView,
)


urlpatterns = [
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('user/register/', RegisterView.as_view(), name='register_user'),
    path('user/login/', TokenObtainPairView.as_view(), name='login_user'),    
    #path('user/login/', LoginView.as_view(), name='login_user'),
    path('user/logout/', LogoutView.as_view(), name='logout_user'),
    path('user/profile/', UserView.as_view(), name='user_details'),
    path('user/reset/', UpdatePasswordView.as_view(), name='user_password'),
]