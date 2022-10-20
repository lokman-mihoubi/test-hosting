import django_filters
from .models import Car
class Carfilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Car
        fields = '__all__'
        exclude = ['image','SLug','price']
