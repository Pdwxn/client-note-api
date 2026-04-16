from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from clients.views import ClientViewSet
from notes.views import NoteViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'notes', NoteViewSet, basename='note')

def home(request):
    return HttpResponse("🚀 Django funcionando correctamente")

urlpatterns = [
    path('', home),
    
    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),

    path('api/auth/', include('rest_framework.urls')),

    path('api/auth/login/', TokenObtainPairView.as_view()),
    path('api/auth/refresh/', TokenRefreshView.as_view()),
]