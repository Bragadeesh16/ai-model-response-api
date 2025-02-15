from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)

urlpatterns = [
    path(
        "api/token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "api/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path("login/", views.login_user, name="login"),
    path(
        "logout/",
        views.logout_user,
        name="logout",
    ),
    path(
        "register/",
        views.user_register,
        name="register",
    ),
]