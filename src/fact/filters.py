import django_filters
from django_filters import DateFilter, CharFilter
from .models import *


class Client_Filter(django_filters.FilterSet):
    class Meta:
        model = Client
        fields = [
            'name',
            'address',
            'phone_no'
        ]


class Staff_Filter(django_filters.FilterSet):
    class Meta:
        model = Client
        fields = [
            'name',
            'address',
            'phone_no'
        ]


class Visitor_Filter(django_filters.FilterSet):
    class Meta:
        model = Client
        fields = [
            'name',
            'address',
            'phone_no'
        ]
