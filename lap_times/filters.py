import django_filters
from .models import TrackTime


class TrackTimeFilter(django_filters.FilterSet):
    class Meta:
        model = TrackTime
        fields = ['name', 'driver', 'event_class']
