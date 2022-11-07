from django.urls import path
from . import views  

# importing of the views from
urlpatterns =[
    path("", views.getRoutes, name="routes")
]