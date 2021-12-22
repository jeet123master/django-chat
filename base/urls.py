from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.LoginPage, name="login-page"),
    path('logout/', views.LogoutUser, name="logout-page"),
    path('register/', views.RegisterUser, name="register-page"),

    path('', views.Home, name="home"),
    path('room/<str:pk>/', views.RoomView, name="room"),
    path('profile/<str:pk>/', views.UserProfile, name="user-profile"),
    path('room-create/', views.CreateRoom, name="create-room"),
    path('update-room/<str:pk>/', views.UpdateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.DeleteRoom, name="delete-room"),
    path('delete-message/<str:pk>/', views.DeleteMessage, name="delete-message"),

]
