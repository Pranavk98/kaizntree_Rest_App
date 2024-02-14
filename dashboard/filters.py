# filters.py
import django_filters
from .models import Item

class ItemFilter(django_filters.FilterSet):
    stock_status = django_filters.CharFilter(lookup_expr='iexact')  # Case-insensitive exact match
    created_at_gte = django_filters.DateFilter(field_name="created_at", lookup_expr='gte')

    class Meta:
        model = Item
        fields = ['stock_status', 'created_at_gte']
