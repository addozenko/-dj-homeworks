from django.urls import path
from .views import MeasurementListCreateView, MeasurementDetailView
from .views import SensorListCreateView, SensorDetailView

urlpatterns = [
       path('measurements/', MeasurementListCreateView.as_view(), name='measurement-list-create'),
       path('measurements/<int:pk>/', MeasurementDetailView.as_view(), name='measurement-detail'),
       path('sensors/', SensorListCreateView.as_view(), name='sensor-list-create'),
       path('sensors/<int:pk>/', SensorDetailView.as_view(), name='sensor-detail'),
   ]
