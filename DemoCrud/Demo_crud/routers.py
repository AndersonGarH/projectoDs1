from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import *

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='User_viewset')
router.register(r'rol', RolViewSet, basename='Rol_viewset')

urlpatterns = [
    path('api/v1/', include(router.urls))
    ]
