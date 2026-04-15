from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from clients.views import ClientViewSet
from notes.views import NoteViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'notes', NoteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),

    path('api/auth/', include('rest_framework.urls')),

    path('api/auth/login/', TokenObtainPairView.as_view()),
    path('api/auth/refresh/', TokenRefreshView.as_view()),
]