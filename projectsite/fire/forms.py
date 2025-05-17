from django.forms import ModelForm
from django import forms
from .models import Locations
from .models import Incident
from .models import FireStation
from .models import Firefighters
from .models import FireTruck
from .models import WeatherConditions


class LocationsForm(ModelForm):
    class Meta:
        model = Locations
        fields = "__all__"


class IncidentsForms(ModelForm):
    class Meta:
        model = Incident
        fields = "__all__"


class FireStationForm(ModelForm):
    class Meta:
        model = FireStation
        fields = "__all__"


class FireFightersForm(ModelForm):
    class Meta:
        model = Firefighters
        fields = "__all__"


class FireTruckForm(ModelForm):
    class Meta:
        model = FireTruck
        fields = "__all__"


class WeatherConditionsForm(ModelForm):
    class Meta:
        model = WeatherConditions
        fields = "__all__"