from django.urls import path
from . import views  
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)


# importing of the views from
urlpatterns =[
    path('users/login/',  views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path("", views.getRoutes, name="routes"),
    path("users/register/", views.registerUser, name="register"),
    path("users/profile/", views.getUserProfile, name="user-profile"),
        path("users/profile/update/", views.updateUserProfile, name="user-profile-update"),

    path("users/", views.getAllUsers, name="users"),

    path("products/", views.getProducts, name="products"),
    path("products/<str:pk>/", views.getProduct, name="product"),

]