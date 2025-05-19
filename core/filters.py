import django_filters
from .models import DDSRecord

class DDSRecordFilter(django_filters.FilterSet):
    date_after = django_filters.DateFilter(field_name="manual_date", lookup_expr='gte')
    date_before = django_filters.DateFilter(field_name="manual_date", lookup_expr='lte')

    class Meta:
        model = DDSRecord
        fields = ['status', 'type', 'category', 'subcategory']
