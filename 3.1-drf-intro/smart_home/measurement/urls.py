from django.urls import path
from .views import SensorListView, SensorDescriptionView, MeasurementView
urlpatterns = [
    path('sensors/', SensorListView.as_view(), name='sensors'),
    path('sensors/<pk>/', SensorDescriptionView.as_view(), name='sensor'),
    path('measurements/', MeasurementView.as_view(), name='measurement'),
]
