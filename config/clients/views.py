from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Client
from .serializers import ClientSerializer
from .filters import ClientFilter

class ClientPagination(LimitOffsetPagination):
    default_limit = 20
    max_limit = 100

class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ClientFilter
    ordering_fields = ['name', 'created_at']
    ordering = ['-created_at']
    pagination_class = ClientPagination

    def get_queryset(self):
        return Client.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)