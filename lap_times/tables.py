import django_tables2 as tables
from .models import TrackTime


class TrackTimeTable(tables.Table):
    class Meta:
        model = TrackTime
        template_name = 'django_tables2/bootstrap.html'
        exclude = ('id', 'tyre')
        order_by = 'best_time'
        # order_by_field = 'sort=best_time&sort'
