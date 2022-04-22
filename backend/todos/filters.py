from django_filters import rest_framework as filters
from .models import Todo


class TodoDateFilter(filters.FilterSet):
    date_created_gte = filters.DateFilter(field_name='created', lookup_expr='gte')
    date_created_lte = filters.DateFilter(field_name='created', lookup_expr='lte')
    date_updated_gte = filters.DateFilter(field_name='updated', lookup_expr='gte')
    date_updated_lte = filters.DateFilter(field_name='updated', lookup_expr='lte')

    class Meta:
        model = Todo
        fields = ['is_active']
