from django.urls import path, re_path, include
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

urlpatterns = [
    path('registration', views.RegistrView.as_view(), name = "registration"),
    path('refresh', TokenRefreshView.as_view(), name='refreshToken'),
    path('logout', views.Logout.as_view(), name = "Logout"),
    path('auth', views.Auth.as_view(), name = "auth"),
    path('takeToken', views.TakeToken.as_view(), name = "takeToken"),
]