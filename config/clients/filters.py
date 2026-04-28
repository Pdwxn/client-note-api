import django_filters
from django.db.models import Q
from .models import Client

class ClientFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='search_filter')
    tags = django_filters.CharFilter(method='tags_filter')

    class Meta:
        model = Client
        fields = ['search', 'tags']

    def search_filter(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) | Q(email__icontains=value)
        )

    def tags_filter(self, queryset, name, value):
        return queryset.filter(tags__contains=[value])