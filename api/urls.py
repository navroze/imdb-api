from django.urls import path, re_path, include
from . import views
from rest_framework import routers

# Create your views here.
router = routers.DefaultRouter()
router.register('movies', views.MovieView)

urlpatterns = [
    path('', include(router.urls)),
]