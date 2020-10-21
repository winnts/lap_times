from django.http import HttpResponse
from django.template import loader
from django_tables2 import SingleTableView
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

from .models import TrackTime
from .tables import TrackTimeTable
from .filters import TrackTimeFilter


# Create your views here.

class TrackTimeView(SingleTableView):
    model = TrackTime
    table_class = TrackTimeTable
    template_name = 'lap_times/tracktime.html'


class FilteredTrackTimeView(SingleTableMixin, FilterView):
    table_class = TrackTimeTable
    model = TrackTime
    template_name = "lap_times/besttimes.html"
    filterset_class = TrackTimeFilter


def index(request):
    track_times_list = TrackTime.objects.order_by('best_time')
    # output = '\n'.join([str(t) for t in track_times_list])
    template = loader.get_template('lap_times/index.html')
    context = {
        'track_times_list': track_times_list,
    }
    return HttpResponse(template.render(context, request))
