from django.urls import path
from .views import (
    RegisterView, 
    LoginView,
    UserProfileView,
    StudentProfileUpdateView,
    InstructorProfileUpdateView,
    UserProfileUpdateView
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('profile/student/', StudentProfileUpdateView.as_view(), name='student-profile'),
    path('profile/instructor/', InstructorProfileUpdateView.as_view(), name='instructor-profile'),
    path('profile/update/', UserProfileUpdateView.as_view(), name='user-profile-update'),
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]