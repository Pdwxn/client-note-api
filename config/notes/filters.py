import django_filters
from django.db.models import Q
from .models import Note

class NoteFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='search_filter')

    class Meta:
        model = Note
        fields = ['client', 'type', 'search']

    def search_filter(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) | Q(content__icontains=value)
        )