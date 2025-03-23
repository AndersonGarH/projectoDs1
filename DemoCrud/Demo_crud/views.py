from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import *


# View del Usuario
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class RolViewSet(ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer