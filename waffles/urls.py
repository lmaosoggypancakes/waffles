from django.urls import path, include
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'posts', views.PostViewSet)
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    # API request routing
    path('auth/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path("", include(router.urls)),
    path("api/posts/<int:id>/", views.update),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]