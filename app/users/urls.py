from django.urls import path
from .views import UserListCreate, UserDetail, MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', UserListCreate.as_view(), name="user-list-create"),
    path('<int:pk>/', UserDetail.as_view(), name="user-detail"),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
