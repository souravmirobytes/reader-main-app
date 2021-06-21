from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('revision/create/', views.CreateBookRevisionAPIView.as_view()),
    path('content/create/', views.CreateBookContentAPIView.as_view()),
    path('create/', views.CreateBookAPIView.as_view()),

    path('revision/<str:pk>/update', views.UpdateBookRevisionAPIView.as_view()),
    path('content/<str:pk>/update', views.UpdateBookContentAPIView.as_view()),
    path('<str:pk>/update', views.UpdateBookAPIView.as_view()),

    path('revision/<str:pk>/view', views.GetBookRevisionAPIView.as_view()),
    path('content/<str:pk>/view', views.GetBookContentAPIView.as_view()),
    path('<str:pk>/view', views.GetBookAPIView.as_view()),
    
    path('revision/', views.ListBookRevisionAPIView.as_view()),
    path('content/', views.ListBookContentAPIView.as_view()),
    path('', views.ListBookAPIView.as_view()),
]
