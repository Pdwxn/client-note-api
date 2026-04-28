from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import Note
from .serializers import NoteSerializer
from .filters import NoteFilter
from .permissions import IsOwner

class NotePagination(LimitOffsetPagination):
    default_limit = 20
    max_limit = 100

class NoteViewSet(ModelViewSet):
    serializer_class = NoteSerializer
    filterset_class = NoteFilter
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'title']
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = NotePagination

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)