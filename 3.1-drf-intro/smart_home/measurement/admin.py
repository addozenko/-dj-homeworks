from django.contrib import admin

from .models import Measurement, Sensor

admin.site.register(Measurement) 
admin.site.register(Sensor)  
