
from django.urls import path

from users.views import StudentViewSet, UserViewSet


urlpatterns = [
    path('', UserViewSet.as_view({'get': 'get_session'}), name='users'),
    path('student', StudentViewSet.as_view({'get': 'get'}), name='student'),
]
