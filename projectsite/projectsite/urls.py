from django.contrib import admin
from django.urls import path

from fire.views import HomePageView, ChartView, PieCountbySeverity, LineCountbyMonth, MultilineIncidentTop3Country, multipleBarBySeverity
from fire.views import FireStationView, FireStationCreateView, FireStationUpdateView, FireStationDeleteView
from fire import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('dashboard_chart/', ChartView.as_view(), name='dashboard-chart'),
    path('PieCountbySeverity/', PieCountbySeverity, name='PieCountbySeverity'),
    path('LineCountbyMonth/', LineCountbyMonth, name='LineCountbyMonth'),
    path('MultilineIncidentTop3Country/', MultilineIncidentTop3Country, name='MultilineIncidentTop3Country'),
    path('multipleBarBySeverity/', multipleBarBySeverity, name='multipleBarBySeverity'),
    path('stations/', views.map_station, name='map-station'),
    path('incident/', views.map_incident, name='map-incident'),
    path("map-station_list", FireStationView.as_view(), name="map-station_list"),
    path("map-station_list/add", FireStationCreateView.as_view(), name="map-station_add"),
    path("map-station_list/<pk>", FireStationUpdateView.as_view(), name="map-station_update"),
    path("map-station_list/<pk>/delete", FireStationDeleteView.as_view(), name="map-station_delete"),

]

