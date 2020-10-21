from django.urls import path
from django.contrib import admin

from . import views
from .views import TrackTimeView
from .views import FilteredTrackTimeView

urlpatterns = [
    path('', views.index, name='index'),
    path('track_times/', TrackTimeView.as_view()),
    path('best_times/', FilteredTrackTimeView.as_view()),
    path('admin/', admin.site.urls),

]
