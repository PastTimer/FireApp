from django.contrib import admin
from django.urls import path

from fire.views import HomePageView, ChartView, PieCountbySeverity, LineCountbyMonth, MultilineIncidentTop3Country, multipleBarBySeverity
from fire.views import FireStationView, FireStationCreateView, FireStationUpdateView, FireStationDeleteView
from fire.views import FirefightersView, FirefightersCreateView, FirefightersUpdateView, FirefightersDeleteView
from fire.views import FiretruckView, FiretruckCreateView, FiretruckUpdateView, FiretruckDeleteView
from fire.views import LocationsView, LocationsCreateView, LocationsUpdateView, LocationsDeleteView
from fire.views import IncidentsView, IncidentsCreateView, IncidentsUpdateView, IncidentsDeleteView
from fire.views import WeatherConditionsView, WeatherConditionsCreateView, WeatherConditionsUpdateView, WeatherConditionsDeleteView
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
    path("firefighters_list", FirefightersView.as_view(), name="firefighters_list"),
    path("firefighters_list/add", FirefightersCreateView.as_view(), name="firefighters_add"),
    path("firefighters_list/<pk>", FirefightersUpdateView.as_view(), name="map-station_update"),
    path("firefighters_list/<pk>/delete", FirefightersDeleteView.as_view(),name="firefighters_delete",),
    path("firetruck_list", FiretruckView.as_view(), name="firetruck_list"),
    path("firetruck_list/add", FiretruckCreateView.as_view(), name="firetruck_add"),
    path("firetruck_list/<pk>", FiretruckUpdateView.as_view(), name="firetruck_update",),
    path("firetruck_list/<pk>/delete", FiretruckDeleteView.as_view(), name="firetruck_delete"),
    path("locations_list", LocationsView.as_view(), name="locations_list"),
    path("locations_list/add", LocationsCreateView.as_view(), name="locations_add"),
    path("locations_list/<pk>", LocationsUpdateView.as_view(), name="locations_update"),
    path("locations_list/<pk>/delete", LocationsDeleteView.as_view(), name="locations_delete"),
    path("incident_list", IncidentsView.as_view(), name="incidents_list"),
    path("incidents_list/add", IncidentsCreateView.as_view(), name="incidents_add"),
    path("incidents_list/<pk>", IncidentsUpdateView.as_view(), name="incidents_update"),
    path("incidents_list/<pk>/delete", IncidentsDeleteView.as_view(), name="incidents_delete"),
    path("weathercondition_list", WeatherConditionsView.as_view(), name="weathercondition_list"),
    path("weathercondition_list/add", WeatherConditionsCreateView.as_view(), name="weathercondition_add"),
    path("weathercondition_list/<pk>", WeatherConditionsUpdateView.as_view(), name="weathercondition_update"),
    path("weathercondition_list/<pk>/delete", WeatherConditionsDeleteView.as_view(), name="weathercondition_delete"),

]

