from django.urls import path, include

# '/user/':
urlpatterns = [
    path('auth/', include('dj_rest_auth.urls'))
]

# ---------- Router ----------
from rest_framework.routers import DefaultRouter
from .views import UserCreateView, UserView
router = DefaultRouter()
router.register('register', UserCreateView) # permissions.AllowAny
router.register('', UserView) # permissions.IsAdminUser
urlpatterns += router.urls