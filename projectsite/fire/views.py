from django.shortcuts import render
from django.views.generic.list import ListView
from fire.models import (Locations, Incident, FireStation, Firefighters, FireTruck, WeatherConditions)

from django.db import connection
from django.http import JsonResponse
from django.db.models.functions import ExtractMonth
from django.db.models import Count
from datetime import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from fire.forms import (LocationsForm, IncidentsForms, FireStationForm, FireFightersForm, FireTruckForm,WeatherConditionsForm)

class HomePageView(ListView):
    model = Locations
    context_object_name = 'home'
    template_name = "home.html"

class ChartView(ListView):
    template_name = 'chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get_queryset(self, *args, **kwargs):
        pass
    
def PieCountbySeverity(request):
    query = '''
    SELECT severity_level, COUNT(*) as count
    FROM fire_incident
    GROUP BY severity_level
    '''
    data = {}
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
    
    if rows:
        data = {severity: count for severity, count in rows}
    else:
        data = {}

    return JsonResponse(data)

def LineCountbyMonth(request):
    
    current_year = datetime.now() .year
    
    result = {month: 0 for month in range(1, 13)}
    
    incidents_per_month = Incident.objects.filter(date_time__year=current_year) \
        .values_list('date_time', flat=True)
        
    for date in incidents_per_month:
        month = date.month
        result[month] += 1
    
    month_names = {
        1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
    }
    
    result_with_month_names = {
        month_names[int(month)]: count for month, count in result.items()
    }
    
    return JsonResponse(result_with_month_names)

def MultilineIncidentTop3Country(request):
    query='''
    
    	SELECT
        fl1.country,
        strftime('%m', fi.date_time) AS month,
        COUNT(fi.id) AS incident_count
    FROM 
        fire_incident fi
    JOIN
        fire_locations fl1 ON fi.location_id = fl1.id
    WHERE
        fl1.country IN (
            SELECT
                fl_top.country
            FROM
                fire_incident fi_top
            JOIN
                fire_locations fl_top ON fi_top.location_id = fl_top.id
            WHERE
                strftime('%Y', fi_top.date_time) = strftime('%Y', 'now')
            GROUP BY fl_top.country
            ORDER BY COUNT(fi_top.id) DESC
            LIMIT 3
        )
        AND strftime('%Y', fi.date_time) = strftime('%Y', 'now')
    GROUP BY fl1.country, month
    ORDER BY fl1.country, month;
    
    '''

    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()

    result = {}

    months = [str(i).zfill(2) for i in range(1, 13)]

    for row in rows:
        country = row[0]
        month = row[1]
        total_incidents = row[2]

        if country not in result:
            result[country] = {month: 0 for month in months}

        result[country][month] = total_incidents

    while len(result) < 3:
        fake_country = f"Country {len(result) + 1}"
        result[fake_country] = {month: 0 for month in months}

    for country in result:
        result[country] = dict(sorted(result[country].items()))

    return JsonResponse(result)

def multipleBarBySeverity(request):
    query = '''
        SELECT
            fi.severity_level,
            strftime('%m', fi.date_time) AS month,
            COUNT(fi.id) AS incident_count
        FROM
            fire_incident fi
        GROUP BY fi.severity_level, month
    '''
    
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()

    result = {}
    months = set(str(i).zfill(2) for i in range(1, 13))

    for row in rows:
        level = str(row[0]) 
        month = row[1]
        total_incidents = row[2]

        if level not in result:
            result[level] = {month: 0 for month in months}

        result[level][month] = total_incidents

    for level in result:
        result[level] = dict(sorted(result[level].items()))

    return JsonResponse(result)

def map_station(request):
     fireStations = FireStation.objects.values('name', 'latitude', 'longitude')
 
     for fs in fireStations:
         fs['latitude'] = float(fs['latitude'])
         fs['longitude'] =  float(fs['longitude'])
 
     fireStations_list = list(fireStations)
     context = {
         'fireStations': fireStations_list,
     }
     return render(request, 'map_station.html', context)
 
def map_incident(request):
    incidents = Incident.objects.values(
        'location__latitude',
        'location__longitude',
        'location__city',
        'severity_level',
        'description'
    )
    cities = Locations.objects.values_list('city', flat=True).distinct()
    
    incident_data = []
    for i in incidents:
        lat = i['location__latitude']
        lon = i['location__longitude']
        city = i['location__city']

        if lat is None or lon is None or city is None:
            continue 
        
        incident_data.append({
            'latitude': float(lat),
            'longitude': float(lon),
            'city': city,
            'severity': i['severity_level'],
            'description': i['description'],
        })
    
    context = {'incidents': incident_data, 'cities': cities}
    return render(request, 'map_incident.html', context)

## Firestation CRUD

class FireStationView(ListView):
    model = FireStation
    context_object_name = "Fire Station"
    template_name = "map-station_list.html"
    paginate_by = 5


class FireStationCreateView(CreateView):
    model = FireStation
    form_class = FireStationForm
    template_name = "map-station_add.html"
    success_url = reverse_lazy("map-station_list")


class FireStationUpdateView(UpdateView):
    model = FireStation
    form_class = FireStationForm
    template_name = "map-station_edit.html"
    success_url = reverse_lazy("map-station_list")


class FireStationDeleteView(DeleteView):
    model = FireStation
    template_name = "map-station_delete.html"
    success_url = reverse_lazy("map-station_list")

##Firefighter CRUD

class FirefightersView(ListView):
    model = Firefighters
    context_object_name = "Firefighters"
    template_name = "firefighters_list.html"
    paginate_by = 5


class FirefightersCreateView(CreateView):
    model = Firefighters
    form_class = FireFightersForm
    template_name = "firefighters_add.html"
    success_url = reverse_lazy("firefighters_list")


class FirefightersUpdateView(UpdateView):
    model = Firefighters
    form_class = FireFightersForm
    template_name = "firefighters_edit.html"
    success_url = reverse_lazy("firefighters_list")


class FirefightersDeleteView(DeleteView):
    model = Firefighters
    template_name = "firefighters_delete.html"
    success_url = reverse_lazy("firefighters_list")
    
##FireTruck CRUD

class FiretruckView(ListView):
    model = FireTruck
    context_object_name = "Firetruck"
    template_name = "firetruck_list.html"
    paginate_by = 5


class FiretruckCreateView(CreateView):
    model = FireTruck
    form_class = FireTruckForm
    template_name = "firetruck_add.html"
    success_url = reverse_lazy("map-station_list")


class FiretruckUpdateView(UpdateView):
    model = FireTruck
    form_class = FireTruckForm
    template_name = "firetruck_edit.html"
    success_url = reverse_lazy("map-station_list")


class FiretruckDeleteView(DeleteView):
    model = FireTruck
    template_name = "firetruck_delete.html"
    success_url = reverse_lazy("firetruck_list")
    
##Locations CRUD

class LocationsView(ListView):
    model = Locations
    context_object_name = "Locations"
    template_name = "locations_list.html"
    paginate_by = 5


class LocationsCreateView(CreateView):
    model = Locations
    form_class = LocationsForm
    template_name = "locations_add.html"
    success_url = reverse_lazy("locations_list")


class LocationsUpdateView(UpdateView):
    model = Locations
    form_class = LocationsForm
    template_name = "locations_edit.html"
    success_url = reverse_lazy("locations_list")


class LocationsDeleteView(DeleteView):
    model = Locations
    template_name = "locations_delete.html"
    success_url = reverse_lazy("locations_list")