from django.urls import path, include
# from django.contrib import admin
from django.contrib.auth import views as auth_views
from Auth import views

urlpatterns = [
    path('', views.home, name="home"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('login/', views.login, name='login'),
    path('social_auth/', include('social_django.urls', namespace='social'))
]
