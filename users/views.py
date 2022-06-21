from rest_framework import viewsets, response, status


from users.permissions import StudentReadAccessPermission
from .serializers import UserSerializer, UserCreateSerializer
from .models import User

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    authentication_classes = [SessionAuthentication,]
    permission_classes = [IsAuthenticated,]

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer
    
    
    def get_session(self, request,  *args, **kwargs):
        try:
            user = User.objects.get(email=request.GET.get('email'))
        except User.DoesNotExist:
            user = None
        
        if user:
            return response.Response(
                data=self.get_serializer_class().to_representation(user),
                status=status.HTTP_200_OK
            )

    
class StudentViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    authentication_classes = [SessionAuthentication,]
    permission_classes = [IsAuthenticated,]
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ["get"]:
            permission_classes = [StudentReadAccessPermission]
        return super().get_permissions()

    def get(self, request, *args, **kwargs):
        if request.user.is_staff and User.objects.filter(role__name='AdminRole').exists():
            return response.Response(
                data=self.serializer_class(request.user).data,
                status=status.HTTP_200_OK
            )
        return response.Response(
            data={'error': 'You are not a student'},
            status=status.HTTP_400_BAD_REQUEST
        )
