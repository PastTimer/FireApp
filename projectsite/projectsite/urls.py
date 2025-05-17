from django.contrib import admin
from django.urls import path

from fire.views import HomePageView, ChartView, PieCountbySeverity, LineCountbyMonth, MultilineIncidentTop3Country, multipleBarBySeverity
from fire.views import FireStationView, FireStationCreateView, FireStationUpdateView, FireStationDeleteView
from fire.views import FirefightersView, FirefightersCreateView, FirefightersUpdateView, FirefightersDeleteView
from fire.views import FiretruckView, FiretruckCreateView, FiretruckUpdateView, FiretruckDeleteView
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
    path("firefighters_list/<pk>", FirefightersUpdateView.as_view(), name="firestation_update"),
    path("firefighters_list/<pk>/delete", FirefightersDeleteView.as_view(),name="firefighters_delete",),
    path("firetruck_list", FiretruckView.as_view(), name="firetruck_list"),
    path("firetruck_list/add", FiretruckCreateView.as_view(), name="firetruck_add"),
    path("firetruck_list/<pk>", FiretruckUpdateView.as_view(), name="firetruck_update",),
    path("firetruck_list/<pk>/delete", FiretruckDeleteView.as_view(), name="firetruck_delete"),

]

